#3주차 과제 (입력 진수 결정 과제)
sel=int(input()) #구하고자 하는 진법 선택(2,10,8,16)
num=input() #숫자를 선택

if sel == 16:
    num10=int(num,16)
if sel == 10:
    num10=int(num,10)
if sel == 8:
    num10=int(num,8)
if sel == 2:
    num10=int(num,2)
    
print(hex(num10))
print(num10)
print(oct(num10))
print(bin(num10))