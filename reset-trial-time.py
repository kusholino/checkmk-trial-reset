from trashSite import createSite, rmSite, copyFile

sitename = "sitename"
with open(sitename, 'r') as file:   #reads out sitename used 
    site = file.read()

time = "time"
with open(time, 'r') as file:   #reads out remaining time
    time = file.read()

numeric_part = ''.join(filter(str.isdigit, time))   #split the numbers from the string
number = int(numeric_part)  #saves numbers as integer

print("Remaining Trial Time:", time)
print("Sitename:", site)

if number <= 15:
    createSite()    #creates Throwaway Site
    copyFile(site)  #replaces date file
    rmSite()        #removes Throaway Site 