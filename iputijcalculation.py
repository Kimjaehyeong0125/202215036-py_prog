i=int(input("1또는 2의 숫자를 입력하시오"))

if i == 1:
    num_i=input("수식 입력")
    print(eval(num_i))

elif i==2:
    num_1=int(input("첫번쨰 숫자를 입력"))
    num_2=int(input("두번째 숫자를 입력"))
    total = 0
    for j in range(num_1,num_2+1):
        total=total+j
    print(f"{num_1} +...+ {num_2} = {total}")

else:
    print("1또는2만 입력")