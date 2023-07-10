import subprocess
from trashSite import createSite, rmSite, copyFile

sitename = "sitename"
with open(sitename, 'r') as file:
    site = file.read()

time = "time"
with open(time, 'r') as file:
    time = file.read()

trash = 'test'
print("Remaining Trial Time:", time)

if time == "15 days":
    createSite(trash)
    copyFile(site, trash)
    rmSite(trash)