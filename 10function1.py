'''
함수   
    형식]  
        def 함수명(매개변수1, 매개변수2):
            실행부
            return 결과1, 결과2
    - 반환값이 없는 함수면 return 값 생략
    - 2개이상의 결과는 콤마로 구분하며 튜플로 반환된다.
'''
#메뉴출력 및 선택용 함수
def menu():
    print('[메뉴중 숫자를 선택하세요]:')
    print('1.덧셈 2.뺄셈 3.곱셈 4.나눗셈')
    print('5.종료')
    return input('번호선택:') #사용자가 입력한 번호 반환

def add(a,b):
    print(a, "+", b, '=', a+b)
def sub(a,b):
    print(a, "-", b, '=', a-b)
def mul(a,b):
    print(a, "*", b, '=', a*b)
def div(a,b):
    print(a, "/", b, '=', a/b)

#loop가 1일때 지속적으로 수행가능한 반복문 생성(무한루프)
loop = 1
choice = 0
while loop==1:
    choice = int(menu()) #메뉴출력 및 번호입력
    if choice == 1:
        add(int(input("덧셈 a= ")), int(input("b=")))
    elif choice == 2:
        sub(int(input("뺄셈 a= ")), int(input("b=")))
    elif choice == 3:
        mul(int(input("곱셈 a= ")), int(input("b=")))
    elif choice == 4:
        div(int(input("나눗셈 a= ")), int(input("b=")))
    elif choice == 5: #사용자가 5를 입력하면 while탈출
        loop = 0
    else:
        print("※1~5까지만 입력하세요※")
print("연산 종료!")        

print("=======================================")

#2개 이상의 반환값을 가진 함수 정의
def min_max(num):
    sum = 0 
    #튜플의 원소를 더해 누적합 저장
    for val in num:
        sum += val
    #파이썬에 저장된 최대값max(), 최소값min()함수를 통해 결과 반환
    return sum, min(num), max(num)

#인자로 사용할 튜플 변수
numbers = (8,7,6,8,4,9,5)

#반환값의 개수만큼 변수를 선언한 후 함수 호출
sumval, minval, maxval = min_max(numbers)
print("튜플의 합, 최대값, 최소값:", sumval, minval, maxval)
