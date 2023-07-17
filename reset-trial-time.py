import subprocess
import time

while True:
    try:
        with open("sitename", 'r') as file:
            site = file.read()
    except FileNotFoundError:
        print("Error: 'sitename' file not found.")
        exit()

    time = "time"
    try:
        with open(time, 'r') as file:
            time = file.read()
    except FileNotFoundError:
        print("Error: 'time' file not found.")
        exit()

    numeric_part = ''.join(filter(str.isdigit, time))
    number = int(numeric_part)

    print("Remaining Trial Time:", time)
    print("Sitename:", site)

    if number <= 15:
        command = f'restore_trial.py -H localhost -s {site}'
        subprocess.run([command], shell = True, text = True)
    time.sleep(10800)

