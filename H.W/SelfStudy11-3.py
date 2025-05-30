outFp=None
outStr=""

filename = input("저장할 파일명을 입력하세요: ")

outFp=open("C:\\Users\\dktm9\\Downloads\\COOKBOOK 2.txt","w")

while True :
    outStr = input("내용 입력:")
    if outStr !="":
        outFp.writelines(outStr+"\n")
    else :
        break
    
outFp.close()
print("---정상적으로 파일에 씀---")