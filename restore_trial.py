import argparse #used for the parameters
import time #used for sleep
from banner import bann #imports banner variable from file banner
from trashSite import createSite, rmSite, copyFile #imports functions from file trashSite
from scrapeSite import scrapeWeb, scrapeVers    #imports functions from file scrapeSite
from colors import reset    #imports reset ascii code for the color reset used in printouts

def main(site, host):
    print(bann) #print banner
    number = scrapeWeb(host, site)  #gets remaining time
    print("Remaining Time:", number+reset)  #prints remaining time 
    print("Checkmk Version:",scrapeVers(host, site))    #gets version and prints it

    if site:    #if parameter site is used
        if host:    #if parameter host is used

            with open("sitename", 'w') as file: #writes used sitename to file for the service to use
                file.write(site)

                createSite()    #creates throwaway site
                time.sleep(1)   #timer 
                copyFile(site)  #replaces date file
                rmSite()        #removes throwaway site
                number = scrapeWeb(host, site)  #gets new remaining time
                print("The time has been reset to:", number+reset)  #prints new remaining time
                 
        else:
            print("No Host/IP was given. Use -H or --host") #if parameter host is missing
    else:
        print("No Site was given. Use -s or --site")    #if parameter site is missing

if __name__ == "__main__":
    parser =argparse.ArgumentParser(description="checkmk trial time reset script")
    parser.add_argument("-s", "--site", nargs = "?", const = True, help = "Enter the site name")    #parameter declaration
    parser.add_argument("-H", "--host", nargs = "?", const = True, help = "Enter Hostname or IP-Adress of the CheckMK Server") #parameter declaration
    args = parser.parse_args()
    main(args.site, args.host)