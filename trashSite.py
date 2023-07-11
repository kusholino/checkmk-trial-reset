import subprocess		#used to run commands and check for errors
from colors import red, green, reset	#imports colors and reset for printouts

def createSite():	#creates throwaway site
	try:
		#creating the one time site
		subprocess.run(["omd", "create", "test"], capture_output=True, text=True, check=True)
		print("Created New Site ...", green+"OK", reset)

	except subprocess.CalledProcessError as e:
		print(red+"Error Creating Site...Error Code:",reset, e)

	try:
		#starting the one time site
		subprocess.run(["omd", "start", "test"], capture_output=True, text=True, check=True)
		
	except subprocess.CalledProcessError as e:
		print(red+"Error starting Site...Error Code:",reset, e)

def copyFile(site):
	file_destination = f'/omd/sites/{site}/var/check_mk/licensing/state_file_created'	#file path of existing site
	file_source = '/omd/sites/test/var/check_mk/licensing/state_file_created'	#file path of throwaway site
	
	try:
		#replacing the stae_file_created file
		subprocess.run(["cp", "-r", file_source, file_destination], capture_output=True, text=True, check=True)
		print("Replaced File ......", green+"OK", reset)

		#give the site user the permission to write and read from the replaced file
		subprocess.run(["chown", site, file_destination], capture_output=True, text=True, check=True) 
		print("Gave Permisions ......", green+"OK", reset)
    
	except subprocess.CalledProcessError as e:
		print(red+"Error Replacing File ... Error Code:",reset, e)

def rmSite():
	command = f'omd rm test'	#command to remove throwaway site
	confirmation = 'yes\n'		#used for automatic confirmation w out userinput

	#removing throwaway site / cleanup after reseting timer
	process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	process.communicate(input=confirmation.encode())

	if process.returncode == 0:
		print("Removed Site .......", green+"OK", reset)
		subprocess.run(["omd", "restart", "sec"])	#restarting existing site (necessary)
		print("Restarted Site .....", green+"OK", reset)
		print(green+"Successfully Reset Trial Time", reset)   
	else:
		print("Removed Site .......", red+"Error", reset)
		print(red+"Error Reseting the Trial Time")