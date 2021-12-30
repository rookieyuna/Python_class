
'''
#지역변수/전역변수
    :파이썬에서는 변수 선언 시 자료형을 기술하지 않으므로
    아래 같은 경우 total은 서로 다른 변수가 된다.
'''
total=0
def sum(arg1, arg2):
    total = arg1 + arg2
    print("지역변수 total=", total)
    return total

print("전역변수 total=", total) #선언한 초기값 0 출력
print("sum(10,20) 호출 후 반환값=", sum(10, 20)) #함수내의 결과 30이 출력
print("==========================")


'''
#내부함수
    :파이썬은 함수내부에 또 다른 함수를 선언할 수 있다
    형식]
        def 함수명1():
            실행문
            def 함수명2():
                실행문
'''
def commander(saying):
    def inner(quote): #내부함수 정의
        return "조선의 위대한 장군 = '%s'" % quote
    return inner(saying) #2차호출
print(commander('이순신')) #1차호출
print("==========================")

'''
매개변수를 전달하는 방식에는 4가지가 있다
1. 순서 매개변수 : 함수에서 사용하는 일반적인 매개변수로 작성순대로 전달
'''
def printme(str1, str2):
    print(str1, str2)
    return
cont = "은 매우 좋은 프로그램입니다."
printme("Python", cont) #=Python 은 매우 좋은 프로그램입니다.
print("==========================")


#2.키워드 매개변수 : 순서에 상관 없이 매개변수명에 따라 전달된다.
def printinfo(name, age):
    print("이름:", name)
    print("나이:", age)
    return
printinfo(age=50, name='홍길동')
print("==========================")


#3.기본매개변수 : 인수가 전달되지 않는 경우 디폴트로 지정되는 값을 말한다.
def defaultArgs(lan="Java"):
    print("내가 좋아하는 언어는 ", lan, "입니다")
    return
defaultArgs() #= Java 입니다 (Java에서는 오류나는 호출-인자가없어서)
defaultArgs("C++") #= C++ 입니다


'''
#4.가변매개변수
    :여러개의 매개변수를 전달해야 할 떄 사용하는 매개변수로
    Java의 가변인자와 비슷하다
    * 사용:  매개변수 값을 튜플로 그룹화
    ** 사용: 매개변수를 딕셔너리로 사용
'''
def product(*args):
    print("*args=>", args) #=(1, 2, 3, 4) ...튜플형태 출력
    result = 0
    for a in args: #튜플이므로 반복문 사용
        result += a
    return result
print("product(1,2,3,4) =", product(1,2,3,4)) #= 10

def famousMan(**man):
    print('**man', man) #={'의인':'홍길동', '장군':'이순신'...딕셔너리 형태 출력
    for key in man:
        print(key, "=>", man[key])
famousMan(의인='홍길동', 장군='이순신', 임금='세종대왕')