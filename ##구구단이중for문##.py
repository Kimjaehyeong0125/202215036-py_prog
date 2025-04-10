##전역 변수 선언 부분##
i,k,guguline = 0,0,""

##메인 코드 부분##
for i in range(2,10):
    guguline=guguline + ("#  %d단  #" %i)
    
print(guguline)
    
for i in range(1,10) :
    guguline=""
    for k in range(2,10) :
        guguline = guguline + str("%2dX%2d=%2d" %(k,i,k*i))
    print(guguline)
#%d 정수형 포멧팅으로 %2d를 넣으면 최소 2칸 너비로 정수를 출력한다는 의미(정렬을 위해서 사용용)