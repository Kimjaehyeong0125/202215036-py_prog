inFp,outFp=None,None
inStr=""

sourceFileName = input("소스 파일명을 입력하세요: ")
targetFileName = input("타깃깃 파일명을 입력하세요: ")

inFp=open("C:\\Users\\dktm9\\Downloads\\COOKBOOK 3.ini","r")
outFp=open("C:\\Users\\dktm9\\Downloads\\COOKBOOK 3.txt","w")

inList=inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)
    
inFp.close()
outFp.close()

print("---파일이 정상상적으로 복사되었음---")
print("---C:\\Users\\dktm9\\Downloads\\COOKBOOK 3.ini 파일이 C:\\Users\\dktm9\\Downloads\\COOKBOOK 3.txt으로 복사되었음음")