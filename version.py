import subprocess
from colors import red, green, reset

def version():
    try:
        version = subprocess.run(["omd", "version"], capture_output=True, text=True, check=True)
        return version.stdout
    except subprocess.CalledProcessError as version:
        print(red+"Error fetching Version...Error Code:",reset, version)