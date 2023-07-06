import subprocess

site_name = 'test'
file_destination = '/root/sec/var/check_mk/licensing/state_file_created'
file_source = f'/omd/sites/{site_name}/var/check_mk/licensing/state_file_created'
command = f'omd rm {site_name}'
confirmation = "yes\n"

#colors for Prints
green = '\033[32m'
red = '\033[31m'
reset = '\033[0m'


print("              ____           _                _____     _       _  ")
print("             |  _ \ ___  ___| |_ ___  _ __ __|_   _| __(_) __ _| | ")
print("             | |_) / _ \/ __| __/ _ \| '__/ _ \| || '__| |/ _` | | ")
print("             |  _ <  __/\__ \ || (_) | | |  __/| || |  | | (_| | | ")
print("             |_| \_\___||___/\__\___/|_|  \___||_||_|  |_|\__,_|_| ")
print("")

#create new site
subprocess.run(["omd", "create", "test"])

print("Created New Site ...", green+"OK", reset)

#replace file
subprocess.run(["cp", "-r", file_source, file_destination, "-v"])

print("Replaced File ......", green+"OK", reset)

process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
process.communicate(input=confirmation.encode())

if process.returncode == 0:
    print("Removed Site .......", green+"OK", reset)
    print("\033[32m{}\033[0m".format("Successfully Reset Trial Time"))
    
else:
    print("Removed Site .......", red+"Error", reset)
    print(red+"Error Reseting the Trial Time")
