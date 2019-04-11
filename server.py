import os
import time

fileName = "msg.txt"
fileDate = os.path.getmtime(fileName)

def loop(fileDate, fileName):
    newFileDate = os.path.getmtime(fileName)
    print(str(fileDate) + " " + str(newFileDate))
    if(newFileDate != fileDate):
        f = open(fileName,"r")
        text = f.read()
        f.close
        print("Massage Reçu : \n" + text)
    return(newFileDate)

while(1):
    fileDate = loop(fileDate, fileName)
    time.sleep(1)
