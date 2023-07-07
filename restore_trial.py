import subprocess
import requests
import argparse
from bs4 import BeautifulSoup
from banner import bann
from trashSite import createSite, rmSite, copyFile
from scrapeSite import scrapeWeb

def main(site, host):
    print(bann)
    #scrapeWeb(host, site)
    print(scrapeWeb(host, site))

    if site:
        if host:
            
            with open("sitename", 'w') as file:
                file.write(site)

                createSite()
                copyFile()
                rmSite()
 
        else:
            print("No Host/IP was given. Use -H or --host")
    else:
        print("No Site was given. Use -s or --site")

if __name__ == "__main__":
    parser =argparse.ArgumentParser(description="checkmk trial time reset script")
    parser.add_argument("-s", "--site", nargs = "?", const = True, help = "Enter the site name")
    parser.add_argument("-H", "--host", nargs = "?", const = True, help = "Enter Hostname or IP-Adress of the CheckMK Server")
    args = parser.parse_args()
    main(args.site, args.host)