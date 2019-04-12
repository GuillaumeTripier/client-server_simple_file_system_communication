import os
import time

fileName = "msg.txt"
fileDate = os.path.getmtime(fileName)

def response(fileDate, fileName, text):
    f = open(fileName,"w")
    f.write("OK 200\ntext length : " + str(len(text)))
    f.close()

def loop(fileDate, fileName):
    newFileDate = os.path.getmtime(fileName)
    print(str(fileDate) + " " + str(newFileDate))
    if(newFileDate != fileDate):
        f = open(fileName,"r")
        text = f.read()
        f.close
        assert(text == "Hello world")
        print("Massage Reçu : \n" + text)
        response(fileDate, fileName, text)
        newFileDate = os.path.getmtime(fileName)
    return(newFileDate)

while(1):
    fileDate = loop(fileDate, fileName)
    time.sleep(1)
