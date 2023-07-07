import subprocess
from colors import red, green, reset

def createSite():
	subprocess.run(["omd", "create", "test"])
	print("Created New Site ...", green+"OK", reset)
	subprocess.run(["omd", "start", "test"])
def copyFile(site):
    file_destination = f'/root/{site}/var/check_mk/licensing/state_file_created'
    file_source = f'/omd/sites/test/var/check_mk/licensing/state_file_created'

    #copy the Time File
    subprocess.run(["cp", "-r", file_source, file_destination])
    print("Replaced File ......", green+"OK", reset)

def rmSite():
	command = f'omd rm test'
	confirmation = 'yes\n'

	process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	process.communicate(input=confirmation.encode())

	if process.returncode == 0:
		print("Removed Site .......", green+"OK", reset)
		subprocess.run(["omd", "restart", "sec"])
		print("Restarted Site .....", green+"OK", reset)
		print(green+"Successfully Reset Trial Time", reset)   
	else:
		print("Removed Site .......", red+"Error", reset)
		print(red+"Error Reseting the Trial Time")