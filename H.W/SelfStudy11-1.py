inFp=None
inStr=""

inFp=open("C:\\Users\\dktm9\\Downloads\\COOKBOOK.txt","r",encoding="utf8")

line_num = 1
while True :
    inStr = inFp.readline()
    if inStr=="":
        break;
    print("%d:%s"%(line_num, inStr),end="")
    line_num += 1
    
inFp.close()