'''
class생성
    형식]
        class 클래스이름:
            def 메서드(self):
                코드

인스턴스 변수
    :메서드 안에 정의되는 변수
    -클래스 내부에서는 self.변수명 형태로 접근한다
    -클래스 외부에서는 객체변수.인스턴스변수 형태로 접근한다.
인스턴스 메서드
    :인스턴스 변수에 항상 접근할 수 있도록 메서드의 첫번째
    파라미터에 객체자신을 의미하는 self를 선언해야 한다.
'''

#클래스 선언
class FourCalculator:
    #setter()메서드로 초기화 담당
    def setdata(self, first, second):
        #self.멤버변수 = 매개변수 형태로 기술됨
        self.first = first
        self.second = second
        
    #사칙연산을 수행하는 인스턴스 메서드 정의.
    #멤버변수 접근을 위해 첫번째 파라미터는 반드시 self로 지정
    def addition(self):
        result = self.first + self.second
        return result
    def subtraction(self):
        result = self.first - self.second
        return result
    def multiplication(self):
        result = self.first * self.second
        return result
    def division(self):
        result = self.first / self.second
        return result

#class 객체 생성. 파이썬에서는 new를 사용하지않는다
a = FourCalculator()
b = FourCalculator()

#각 객체의 setter() 메서드를 통해 인스턴스 변수 초기화
a.setdata(4,2)
b.setdata(3,8)

#각 객체의 인스턴스 메서드 호출
print("객체a 덧셈", a.addition())
print("객체a 뺄셈", a.subtraction())
print("객체b 곱셈", b.multiplication())
print("객체b 나눗셈", b.division())

'''
생성자(initializer)
    : 클래스로부터 객체를 만들 때 인스턴스 변수를 초기화한다.
    init양쪽에 언더바 2개를 붙여 정의한다.
정젹메소드 
    : 클래스 명으로 바로 접근할 수 있는 메소드를 말한다
        @staticmethod 데코레이터를 사용한다
클래스 메소드 
    : 정적메소드와 비슷한데, 객체 인스턴스를 의미하는 self대신
        클래스를 의미하는 cls 파라미터를 전달받는다.
        cls를 통해 클래스변수에 접근할 수 있다.
        @classmethod 데코레이터를 사용한다
'''

class CalculatorInit:
    #클래스 변수(클래스 전체에서 접근가능한 전역변수)
    count = 0
    
    #파이썬에서는 Java처럼 생성자 오버로딩은 지원하지 않는다.
    '''
    def __init__(self):
        self.first = 1
        self.second = 2'''
    
    #생성자 메서드 정의. 멤버변수 초기화를 위해 첫번째 파라미터 self 필수
    def __init__(self, first, second):
        self.first = first
        self.second = second
        #생성자에서 클래스 변수 접근 가능
        CalculatorInit.count += 1
    
    #일반적인 인스턴스 메서드 정의
    def addition(self):
        result = self.first + self.second
        return result
    
    #정적메서드 정의. 클래스명으로 즉시 호출 가능
    @staticmethod
    def staticArea(pFirst, pSecond):
        result = pFirst * pSecond
        print("static메소드", result)
    
    #클래스메서드 정의. cls를 통해 클래스변수에 접근 가능
    @classmethod
    def showInfo(cls):
        print('class메소드', cls.count)
        
#fCal2 = CalculatorInit() #=> 기본생성자 없어서 에러발생 
#2개의 인자를 전달해서 객체 생성
fCal = CalculatorInit(2010, 43)
#일반적인 인스턴스 메서드 호출
print(fCal.addition())  
#클래스메서드 호출1 : 인스턴스 변수를 통한 호출
fCal.showInfo()
#클래스메서드 호출2 : 클래스명을 통한 호출
CalculatorInit.showInfo()
#정적메서드 호출
CalculatorInit.staticArea(5, 8)


#상속 : 파이썬에는 별도의 키워드없이 클래스 정의시 매개변수형태로 상속    
class MoreCaculator(CalculatorInit):
    #자식쪽에서 확장한 인스턴스 메서드
    def pow(self):
        #first를 second만큼 거듭제곱한다
        result = self.first ** self.second
        return result
    #오버라이딩 : 부모의 기능을 자식쪽에서 재정의
    def addition(self):
        return (self.first + self.second) * 2

#자식객체 생성 및 호출
moreCal = MoreCaculator(4, 3)
print("상속후", moreCal.pow()) #4의 3승 결과 출력

#부모 객체 및 자식객체 생성
p1 = CalculatorInit(100, 200)
p2 = MoreCaculator(100, 200)
#오버라이딩 결과 확인
print("부모객체로호출", p1.addition()) #=300
print("자식객체로호출", p2.addition()) #=600

#정보은닉 : 인스턴스 변수를 비공개 속성(private)으로 설정
class Person:
    def __init__(self, n, a, pw):
        self.name = n
        self.age = a
        #__변수명으로 선언시 private 변수가 된다
        self.__password = pw #생성자에서 초기화함
        
    #password변수 getter()메서드의 역할
    def secret_info(self):
        return self.__password 

p1 = Person('my', 22, 'qwer1234')
print("이름", p1.name) 
print("나이", p1.age) 

#print("비밀번호1", p1.__password) #private 변수이므로 클래스외부에서 접근불가
#print("비밀번호2", p1.password) #언더바가 없는 형태의 변수가 없어 에러 
print("비밀번호", p1.secret_info()) #getter역할의 메서드를 통해 간접 접근

