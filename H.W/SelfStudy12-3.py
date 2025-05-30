import threading
import time

class SumNumber:
    
    sumNum = ''
    
    def __init__(self,Num):
        self.sumNum = Num
        
    def loopNumber(self) :
        if self.sumNum =="1":
            start, end = 1, 1000
        elif self.sumNum =="2":
            start, end = 1, 100000
        elif self.sumNum =="3":
            start, end = 1, 10000000
        else:
            print("알 수 없는 수")
            return
        
        total = sum(range(start, end + 1))
        print(f"1+2+3+.....+ {end} = {total}입니다.")
        
        
num1=SumNumber('1')
num2=SumNumber('2')
num3=SumNumber('3')

th1=threading.Thread(target=num1.loopNumber)
th2=threading.Thread(target=num2.loopNumber)
th3=threading.Thread(target=num3.loopNumber)

th1.start()
th2.start()
th3.start()

th1.join
th2.join
th3.join