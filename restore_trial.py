import argparse
import time
from banner import bann
from trashSite import createSite, rmSite, copyFile
from scrapeSite import scrapeWeb, scrapeVers
from colors import reset

def main(site, host):
    print(bann)
    number = scrapeWeb(host, site)
    print("Remaining Time:", number+reset)
    print("Checkmk Version:",scrapeVers(host, site))

    if site:
        if host:

            with open("sitename", 'w') as file:
                file.write(site)

                createSite()
                time.sleep(1)
                copyFile(site)
                rmSite()
                number = scrapeWeb(host, site)
                print("Remaining Time:", number+reset)
                 
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