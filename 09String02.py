'''
06String - % 서식문자 (Java의 printf와 비슷)
    형식]
        "정수: %d 실수: %f" % (num1, num2)
        "문자열: %s" % '기쁨'
    => 자리수 지정시 %10d, %5.3f처럼 사용
'''

#문자열 사용
str = '내 이름은 %s 입니다' % '칸'
print("str1=", str)

names = ['유비','관우','장비']
for n in names: #for문에서 리스트의 크기만큼 반복하므로
    print('이름 : %s' % n) #하나의 원소가 매칭된다.
    
#정수 : %d
money = 10000
str = '마우스 가격은 %d원 입니다.' % money
print(str)

#실수 : %f
pi = 3.141592
print('원주율은 %1.2f' % pi)

#문자열 : %s
str = '이름 : %s. 나이 : %d' % ('홍길동', 99) #두개이상의 변수는 콤마로 구분
print(str)

#여러개의 변수를 한번에 초기화시켜서 기술한다
phone, age, height = "010-1234-5678", 28, 181.5
str2 = '전화번호:%s, 나이:%d, 키:%f' % (phone, age, height)
print("str2=", str2)