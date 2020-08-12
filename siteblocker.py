# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 10:55:12 2020
pj: Siteblocker
@author: Hyu1
"""
#Before run this, make sure you run the program to adminstrator (to access to host file)
#Import time.

#import mysql.
import mysql.connector as mysql

db = mysql.connect (
    host = "localhost",
    user = "root",
    passwd = "huypr113"
    )

cursor = db.cursor()

cursor.execute("SELECT")

#Rename datetime as dt.
from datetime import datetime as dt

#Enter directory of the host file. This is for Windows. May different depens on your OS.
hosts_path = "C:\Windows\System32\drivers\etc\hosts" 

#Enter local ip or the ip of the site you want to redirect when the blocked site is opened.
redirect = "127.0.0.1"

#Ask users how many sites they want to block at a time.
#Run it as a loop.
#Append the values in a list.
siteNum = int(input("How many sites you want to block: "))

for i in range (1, siteNum + 1):
    website_list = []
    website = input("Enter the site url to block: ")
    website_list.append(website)
    
#Block the sites for specific timing in a day.
    
#Ask the users for starting and ending time.
startTime = int(input("Enter the starting time to block the site (in 24hr): "))
endTime = int(input("Enter the end time to block the site (in 24hr): "))

#Initiate an infinite loop to check for the time.
while True:
    #In blocking hours.
    if dt(dt.now().year, dt.now().month, dt.now().day, startTime) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, endTime):
        #Open host file.
        with open(hosts_path, 'r+') as file:
            #Read the file content.
            content = file.read()
            for websites in website_list:
                if website in content:
                    pass
                else:
                    #Write the redirect ip + space + website url.
                    file.write(redirect + " " + website + "\n")
    #In free hours.
    else:
        #Remove the blocked site url.
        #Open the host file.
        with open (hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            file.truncate()
            
            
            
                    
        
        
