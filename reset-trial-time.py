import subprocess
from trashSite import createSite, rmSite, copyFile

with open(sitename, 'r') as file:
    site = file.read()

with open(time, 'r') as file:
    time = file.read()

trash = 'test'

if time <= 10:
    createSite(trash)
    copyFile(site, trash)
    rmSite(trash)