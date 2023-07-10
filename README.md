#checkmk-trial-reset

##How it works

Checkmk Trial Reset works by copying the file, which is created when first starting a newly created site, where the encrypted date is saved. The script creates a one time site, which will be deleted after the process is completed. The newly created site has 30 days remaining in the trial. So the script just replaces the old file of your local site with the newly created date file. This tricks Checkmk into thinking the site has just been created.

Please note that Checkmk Trial Reset should only be used for testing or evaluation purposes. It is not intended to be used to bypass licensing restrictions or to use Checkmk without a valid license.

##Installation
1. Clone the repository:
'git clone https://github.com/kusholino/checkmk-trial-reset'

2. Change into the project directory:
'cd checkmk-trial-reset'

3. Install dependencies:
'python3 install-dependencies.py'

4. Run the Script:
'python3 restore_trial.py -s <sitename> -H <hostname/IP-Address>'

**Note**: The script requires Python 3 to be installed on your system.

##Disclaimer

This tool is provided for educational and testing purposes only. Use it responsibly and at your own risk. The author is of this tool is not responsible for any misuse or illegal activities caused by the usage of this tool. This tool is not affiliated with or endorsed by Checkmk.

##Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements please open an issue or submit a pull request.

##Contact

If you have any questions or need assistance, feel free to contact the me:

Email: joachim.stoeckeler@outlook.com

Feel free to reach out with any questions, suggestions or bug reports.