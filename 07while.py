'''
반복문
    :파이썬에서의 반복문은 while문과 for문만 있고 do~while문은 없다
'''


str = 'python'
#str이 공백이 될때까지 반복한다. 공백이 아니면 true를 반환한다
while str:
    #출력문 끝에 공백을 추가하여 줄바꿈 없이 출력한다
    print(str, end=' ')
    #슬라이싱을 통해 제일 앞 문자하나를 제거한 후 str에 대입
    str = str[1:]
print()
print("===================="*3)

'''
    파이썬에서는 while문에 else를 추가할 수 있다.
    while문의 조건이 false일 때 탈출하여 else 구문이 실행된다.
'''
#시나리오] 1~10까지의 합을 구하시오
sum = 0
i = 1
while i<=10:
    sum += i #총합누적
    if i<10:
        print(i, end=" + ")
    else:
        print(i, end=" = ")
    i += 1 #i값 증가(i++이 없으므로 복합연산자 사용)
else:
    #while문을 벗어나면 실행된다.
    print(sum)

print("===================="*3)


#시나리오] 구구단을 짝수단만 출력하시오

dan = 2
while dan<=9 :
    if dan%2 == 1: #단이 홀수일 경우
        dan += 1
        continue #반복문 처음으로 돌아가기
    else: #단이 짝수인 경우
        su = 1
        while su<=9:
            #print()같이 서식문자를 사용할때는 %로 문자열과 변수를 구분한다
            print("%2d * %2d = %2d" % (dan, su, dan*su), end=' ')
            su += 1
    dan += 1
    print()
print()