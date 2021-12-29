#라인단위 주석
'''
블럭단위 주석
(이미 입력된 코드를 드래그 한 후 싱글 쿼테이션 세번 누르면 주석으로 만들 수 있다)
'''

#파이썬은 문장의 끝에 ;(세미콜론)을 사용하지 않는다 
#하지만 한줄에 여러명령어를 쓰는 경우 구분을 위해 써야한다.
print("Hello Python")
print("한줄에"); print("여러줄 쓰려면"); print("세미콜론이 필요함")

print("==========================")
print("여러 변수 선언")
print("==========================")
#좌측항은 변수, 우측항은 할당할 값으로 구분하여 선언 및 초기화한다
r, g, b = "Red", "Green", "Blue"
#여러개의 변수를 출력할 때는 콤마를 통해 구분한다.
print(r, g, b)

print("==========================")
print("정수형")
print("==========================")
#파이썬은 변수 선언시 별도의 데이터형을 붙이지 않는다.
x=2
y=4
z=8

print("x / y", x / y) #나누기. 항상 float형 결과를 반환한다
print("x // y", x // y) #나누기. 소수부분을 제거하므로 항상 int형의 결과를 반환한다
print("x * y", x * y)
print("x ** y", x ** y) #거듭제곱. 2의 4승을 계산한다
print("pow(x, y)", pow(x, y)) #거듭제곱 함수를 통해 거듭제곱을 계산한다
print("pow(x, y, z)", pow(x, y, z)) #2의 4승을 8로 나누는 나머지를 반환한다.
print("divmod(x, y)", divmod(x, y)) #x와 y를 나눈 몫과 나머지를 튜플로 반환한다.

#import는 모듈을 불러올 때 사용하는 명령으로 math모듈을 사용한다는 의미
import math
print("math.factorial(5)", math.factorial(5)) #5! = 120

print("==========================")
print("String형")
print("==========================")
str = """아래와 같이
여러줄에 걸쳐 문자열을 작성하고 싶으면
더블쿼테이션을 3개로 감싸 작성한다
"""
print(str)

head="나는 헤더 "
bottom="나는 바텀"
print(head+bottom) #문자열 합치기(덧셈기호 사용)
print(head*3) #문자열 반복하기(곱셈기호 사용)

#문자열 슬라이싱 : index와 범위를 통해 접근할 수 있다.
engStr = "Hello Python Good"
print(engStr[0]) #index0 : H
print(engStr[:3]) #처음부터 index3앞 : Hel
print(engStr[1:3]) #index1부터 3앞 : el
print(engStr[1:]) #index1부터 끝까지 : ello Python Good

korStr = "안녕하세요? 파이썬입니다"
print(korStr[0]) #안
print(korStr[:2]) #안녕
print(korStr[0:6]) #안녕하세요?

'''
format()
    : 문자열의 format()함수를 사용하면 좀 더 발전된 스타일로 문자열포맷 지정 가능
        (Java의 printf문과 비슷한 형태로 사용이 가능하다.)
'''
#인덱스를 사용하는 방법
print("{0}는 중복되지 않는 숫자 {1}개로 구성된다".format("Lotto", 6))
print("{1}은 중복되지 않는 숫자 {0}개로 구성된다".format("Lotto", 6))

#인덱스 대신 변수를 사용하는 방법. 단 defalut값을 지정할 때는 "변수명=값" 으로 사용한다
menu1 = "치킨"
menu2 = "맥주"
print("오늘 {str}은 {0}과 {1}로 정했다".format(menu1, menu2, str="저녁"))

print("{0}, 오늘 {str}은 너로 정했다".format("지슈슈", str="포켓몬"))
