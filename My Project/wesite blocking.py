from time import *
from datetime import *

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com"]

while True:
    if datetime(datetime.now().year,datetime.now().month,datetime.now().day,12,15)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,12,23):
        with open(host_path,"r+") as fileptr:
            print("Working Hours...")
            content=fileptr.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    fileptr.write(redirect+"       "+website+"\n")
    else:
        with open(host_path,"r+") as file:
            print("Free Time....")
            content=file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    sleep(5)
            
            
