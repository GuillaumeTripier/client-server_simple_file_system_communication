import os
import time

fileName = "msg.txt"
i = 1

def waitingForResponse(fileName, fileDate, textInput):
    i = 0
    while(i == 0):
        newFileDate = os.path.getmtime(fileName)
        print(str(fileDate) + " " + str(newFileDate))
        if(newFileDate != fileDate):
            f = open(fileName,"r")
            text = f.read()
            f.close
            assert(text == "OK 200\ntext length : " + str(len(textInput)))
            print("Server response : \n" + text)
            i += 1
        time.sleep(1)


while(1):
    text = input("Message to send : ")
    f = open(fileName,"w")
    f.write(text)
    f.close()
    fileDate = os.path.getmtime(fileName)
    waitingForResponse(fileName, fileDate, text)
