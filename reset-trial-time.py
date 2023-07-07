import subprocess
from trashSite import createSite, rmSite, copyFile

sitename = "sitename"
with open(sitename, 'r') as file:
    site = file.read()

time = "time"
with open(time, 'r') as file:
    time = file.read()

trash = 'test'
print(time)
if time is False:
    createSite(trash)
    copyFile(site, trash)
    rmSite(trash)