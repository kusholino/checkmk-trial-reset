import subprocess
from colors import colors

def createSite():
	subprocess.run(["omd", "create", "test"])
	print("Created New Site ...", colors.green+"OK", colors.reset)
		
def copyFile():
    file_destination = f'/root/{site}/var/check_mk/licensing/state_file_created'
    file_source = f'/omd/sites/test/var/check_mk/licensing/state_file_created'

    #copy the Time File
    subprocess.run(["cp", "-r", file_source, file_destination])
    print("Replaced File ......", colors.green+"OK", colors.reset)

def rmSite():
	command = f'omd rm test'
	confirmation = 'yes\n'

	process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	process.communicate(input=confirmation.encode())

	if process.returncode == 0:
		print("Removed Site .......", colors.green+"OK", colors.reset)
		subprocess.run(["omd", "restart", "sec"])
		print("Restarted Site .....", colors.green+"OK", colors.reset)
		print(green+"Successfully Reset Trial Time", colors.reset)   
	else:
		print("Removed Site .......", colors.red+"Error", colors.reset)
		print(colors.red+"Error Reseting the Trial Time")