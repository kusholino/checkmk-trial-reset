import subprocess
import argparse
from colors import red, green, reset

def install_beautifulsoup():
    try:
        subprocess.run(["apt-get", "install", "python3-pip3", "-y"], capture_output=True, text=True, check=True)
        subprocess.check_call(["pip3", "install", "beautifulsoup4", "-y"])
        print("Beautiful Soup installed successfully.")
    except subprocess.CalledProcessError:
        print("Installation failed. Please make sure pip is installed and try again.")

# Usage
def main(service):
    install_beautifulsoup()

    try:
        subprocess.run(["cp", "reset-trial-time.service", "/etc/systemd/system"], capture_output=True, text=True, check=True)
        subprocess.run(["cp", "cmk-reset-timer.service", "/etc/systemd/system"], capture_output=True, text=True, check=True)

        subprocess.run(["systemctl", "enable", "cmk-reset-timer.service"], capture_output=True, text=True, check=True)
        subprocess.run(["systemctl", "start", "cmk-reset-timer.service"], capture_output=True, text=True, check=True)

        subprocess.run(["systemctl", "enable", "reset-trial-time.service"], capture_output=True, text=True, check=True)
        subprocess.run(["systemctl", "start", "reset-trial-time.service"], capture_output=True, text=True, check=True)
        print("Installed Service ... ",green+"OK",reset)

    except subprocess.CalledProcessError as e:
        print(red+"Error installing Service ... Error Code: ",reset, e)



if __name__ == "__main__":
    parser =argparse.ArgumentParser(description="install dependencies for checkmk trial reset")
    parser.add_argument("-s", "--service", nargs = "?", const = True, help = "If you want to install the service use -s or --service")
    args = parser.parse_args()
    main(args.service)