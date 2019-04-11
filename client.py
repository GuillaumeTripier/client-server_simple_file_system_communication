
fileName = "msg.txt"
i = 1
while(1):
    text = input("Message to send : ")
    f = open(fileName,"w")
    f.write(text)
    f.close()
