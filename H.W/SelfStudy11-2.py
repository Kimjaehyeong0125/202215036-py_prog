inFp=None
inList,inStr=[],""

inFp=open("C:\\Users\\dktm9\\Downloads\\COOKBOOK.txt","r",encoding="utf8")

line_num = 1
inList = inFp.readlines()
for inStr in inList :
    print("%d:%s"%(line_num, inStr),end="")   
    line_num += 1
    
inFp.close()