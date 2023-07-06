import subprocess
import requests
import argparse
from bs4 import BeautifulSoup
from banner import banner
from trashSite import createSite, rmSite, copyFile
from colors import colors
from scrapeSite import scrapeWeb

def main(site, host, trash):
    print(banner)
    scrapeWeb()
    print(remaining_time)
    print("Version:", foot_text)

    if site:
        if host:
            if trash:
                with open(sitename, 'w') as file:
                    file.write(site)

                    createSite(trash)
                    copyFile(site, trash)
                    rmSite(trash)
            else:
                print("No trash was given. Use -t or --trash")  
        else:
            print("No Host/IP was given. Use -H or --host")
    else:
        print("No Site was given. Use -s or --site")

if __name__ == "__main__":
    parser =argparse.ArgumentParser(description="checkmk trial time reset script")
    parser.add_argument("-s", "--site", nargs = "?", const = True, help = "Enter the site name")
    parser.add_argument("-H", "--host", nargs = "?", const = True, help = "Enter Hostname or IP-Adress of the CheckMK Server")
    parser.add_argument("-t", "--trash", nargs = "?", const = True, help = "Enter any name for a site to excract the file from (Will be deleted automatically)")
    args = parser.parse_args()
    main(args.site, args.host, args.trash)