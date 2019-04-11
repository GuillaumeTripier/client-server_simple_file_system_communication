
fileName = "msg.txt"
while(1):
    text = input()
    f = open(fileName,"w")
    f.write(text)
    f.close()
