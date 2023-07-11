# Checkmk Trial Reset

## How it works

Checkmk Trial Reset works by copying the file, which is created when first starting a newly created site, where the encrypted date is saved. The script creates a one time site, which will be deleted after the process is completed. The newly created site has 30 days remaining in the trial. So the script just replaces the old file of your local site with the newly created date file. This tricks Checkmk into thinking the site has just been created.

### Details
The date file is located in `/omd/sites/<localsitename>/check_mk/licensing/state_file_created` and is encrypted. You will **NOT** be able to copy the content or manipulate it, since its encrypted. You **NEED** to replace it how it is otherwise it wont work. In some cases you will need to give checkmk the permissions to read and write to the file so added it in the script. If you want to do it manually do not forget to restart your local site so the changes take action.

Please note that Checkmk Trial Reset should only be used for testing or evaluation purposes. It is not intended to be used to bypass licensing restrictions or to use Checkmk without a valid license.

## Installation without the Service
1. Clone the repository:
 
   `git clone https://github.com/kusholino/checkmk-trial-reset`

2. Change into the project directory:
 
   `cd checkmk-trial-reset`

3. Install dependencies:
  
   **Debian:** 
 
   `python3 install-dependencies-debian.py`
 
   **Ubuntu:**
 
   `sudo -s`
 
   `python3 install-dependencies-ubuntu.py`

4. Run the Script:
 
   `python3 restore_trial.py -s <sitename> -H <hostname/IP-Address>`

## Installation with Service

The Service checks if the Remaining time fell below 15 days. If it did it automatically runs the script to reset the Timer.
**Note:** Run the Script normally atleast once so the service has the Informations it needs. (local site name and the time)

1. Clone the repository:
 
   `git clone https://github.com/kusholino/checkmk-trial-reset`

2. Change into the project directory:
 
   `cd checkmk-trial-reset`

3. Install dependencies:
 
   **Debian:** 
 
   `python3 install-dependencies-debian.py -s`
 
   **Ubuntu:**
 
   `sudo -s`
 
   `python3 install-dependencies-ubuntu.py -s`

4. Run the Script:
 
   `python3 restore_trial.py -s <sitename> -H <hostname/IP-Address>`

**Note:** The script requires Python 3 to be installed on your system. The file restore_trial.py is the standalone script and the reset-trial-time.py is the script used by the service. This Script is only tested using a debian environment!

## Manually Reseting the trial time

1. Create a one time Site and start it:
 
   `omd create <any sitename>`
 
   `omd start <any sitename>`

3. Replace the file:
 
   `cp /omd/<existing site>/var/check_mk/licensing/state_file_created /omd/<one time site>/var/check_mk/licensing/state_file_created`

4. Remove the one time site and restart the existing site:
 
   `omd rm <any sitename>`
 
   `omd restart <existing site>`

6. Give correct permissions:
 
   `chown <existing site user /omd/<existing site>`

## Tested Features
    - [x] Created Basic Script for Replacing the file
    - [x] Scraping to retrieve Version and Remaining Time
    - [x] Created install Dependency Script
    - [ ] Service for automatic renewing the trial time

## Future Features
    - [x] Supports Ubuntu
    - [ ] Supports Mint
    - [ ] Supports RedHat

## Disclaimer

This tool is provided for educational and testing purposes only. Use it responsibly and at your own risk. The author is of this tool is not responsible for any misuse or illegal activities caused by the usage of this tool. This tool is not affiliated with or endorsed by Checkmk.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements please open an issue or submit a pull request.

## How did i get so far?

1. Reverse Engineering
 
   I started to reverse engineer how the checkmk site counts down the days. My first guess was the website. So i used the HTML Inspect Tool to see if i can find a link to any files. I found out a class called remaining_time exist which is the Counter at the login screen besides the loading bar. From there i tried      to look into the js script of the login screen but with no success.

2. Taking a closer look
 
   I made a backup of my already existing site. Looked thru the files to see if any files could be the file im searching for. After i couldnt find any file within a couple of hours. I created a site in my testlab and tried to copy the subdirectories of my backup into the testlab site. Using this i managed to tell      that when replacing the subdirectory `/var` the Counter is the same as the one from my existing site. With this information i manually copied every subdirectory of `/var` into the testlab site. But for some reason the time did not go to the original one. I was confused and started to exclusively look at the         files in `/var`. I found a subdirectory called licensing which sparked my intrest. In this directory was 1 file that immediatly spiked my intrest `state_file_created`, i instantly thought this must be it since my thought process was that checkmk creates this file once the site has been started for the first         time and checks the trial timer based off of this specific file.

3. Figuring out how to manipulate the date
 
   Upon inspecting the file, i saw its encrypted. I tried to use [CyberChef](https://gchq.github.io/CyberChef/) to check if its any known encryption but with no success. So i tried to copy and paste the content of this file from my backup into a test site within the testlab. Then i first had a major success. After     doing this i had 37649 years left but was out of range (for obvious reasons).

3. Trying to manipulate a backup
 
   A Checkmk backup consists, if not encrypted and not compressed, of a .tar file and a mkbackup.info file. The tar file is a copy of the site u backed up and the mkbackup.info file includes the MD5 Hashvalue of the tar file also its size and when its been created. This was the first time i made a script to unzip      the tar file replace the `state_file_created` file zip it again and calculate its hashvalue and writing this information into the mkbackup.info file. Yet due to my lack of knowledge i couldnt get the script to successfully write the hashvalue and size into mkbackup.info. So i tried it manually which worked. Then    i tried to use the Checkmk Backup feature in the Website but with no success at first, since it was the wrong hashvalue. Thankfully the site returned which hashvalue it expected and so i wrote it into the file. Well that didnt work but the hashvalue error was fixed and another error came up. A broken pipe error.    So i was at the beginning again, since i didnt want to invest time into figuring out the broken pipe error, i tried a different approach which was really simple. Manually replacing the file in the live testlab site.

4. Finish the way how to reset the trial time
 
   After manually replacing the file the time was still not reset. After a restart of the site the remaining days was 30 Days. But it wasnt perfect. After testing if everything worked without issues, i found out a permission error to the file i replaced. Since Checkmk creates a local user for a site this user didnt    have permissions to write or read from this file. So i gave the user the correct permissions and it worked as if i just downloaded and installed the Checkmk Enterprise Trial Version. At this point i thought of making a script to do this for me even tho you can easily do this with 5 lines of commands in your         linux environment. 

5. Creating the Script.
 
   To further learn and test new ways to code. I didnt want to put the whole code into just one simple file. I challenged myself to use different files and import functions or variables. At first i used chatgpt to see how it could be done and then started to code. The first version was crappy with no actual checks     if the script worked or not. I slowly added error checks, parameters that needed to be used and started to think of good ideas what to include into the script for example the Remaining time or the CheckMK Version. For those two i scraped the login screen of your local site, searched for the class                    `remaining_days`, extracted it and splitted the string "28 days" into just "28" for visual reasons. For the Version i searched the id `foot` extracted its content, wrote it into a file and also splitted the content so the Version is displayed correctly. Then i thought a service that checks if the remaining time     exceeded a certain amount of time and then runs the script automatically could be sick. So after having the base construct and working script i started to code the service and made a install dependencies script aswell as a parameter to tell if you want the service installed or not. This whole project took me        alot of time and was a good learning experience. Since i dont really have any experience coding in python and if you have any suggestions what i could have done better, please let me know. Also Checkmk if you want me to take this down just contact me and i will make this repo privat as soon as possible. I will      try and update the script constantly.
