#This parses a file in the downloads directory

jabber = open("/Users/willi/Downloads/sample.txt","r")

for line in jabber:
    print(line)

jabber.close