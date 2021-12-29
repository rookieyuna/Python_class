'''
파일명 : 02List.py

파이썬에는 연속된 Collection 데이터 구조에
list, tuple, dictionary, set 이 있다.

리스트(list)
    : 대괄호[] 안에 콤마로 항목을 구분하며, 대입연산자로 항목을 변경할 수 있는 시퀀스 자료형
    서로 다른 자료형의 항목으로도 구성 가능하다
    - 인덱싱, 슬라이싱, 연결, 반복, 추가, 삭제 등이 가능하다.
    - Mutable 데이터 타입이라고 한다

'''

#기본적인 선언과 사용법은 배열과 동일하다.
#선언
list1 = [1,2,3,4,5]
list2 = ['Java', 'HTML', 'Python']
#중첩된 리스트 선언 가능
list3 = [10, 20, ['Java', 'HTML', 'Python']]

#출력
print('list1:', list1) #리스트 전체가 출력됨
print('list2[2]:', list2[2]) ##'Python'
print('list2[-1]:', list2[-1])##'Python'
print('list3[2]:', list3[2]) #리스트 내의 리스트가 출력됨

#리스트 슬라이싱 
print("===리스트 슬라이싱", "="*30)
print('list1[1:4]:', list1[1:4]) #1~3까지 출력
print('list1[:3]:', list1[:3]) #0~2까지 출력
print('list1[1:]:', list1[1:]) #1~마지막까지 출력

##없는인덱스 슬라이싱 오류Test##
print('list1[9:10]:', list1[0:10]) #[1, 2, 3, 4, 5]만 출력 (오류안남)
print('list1[9:10]:', list1[9:10]) #[] 출력 (오류안남)
#But 인덱싱의 경우 인덱스를 벗어나면 에러
#print('list1[9]:', list1[9]) #list index out of range 오류


#리스트 연결
print("===리스트 연결", "="*30)
all_list = [list1, list2] #새로운 리스트에 기존 리스트를 삽입하여 연결하는 형태
print('all_list:', all_list)
print('all_list[1][0]:', all_list[1][0]) #=Java

print("===list 관련 메소드", "="*30)
list1.append(6) #추가
print('append(6)=>', list1) #=append(6)=> [1, 2, 3, 4, 5, 6]

list1.clear() #전체삭제
print('clear()=>', list1) #=clear()=> []

list1.extend([10,20,30,40,50]) #리스트 확장
print('extend=>', list1) #=extend=> [10, 20, 30, 40, 50]

list1.insert(1,99) #지정인덱스 삽입
print('insert(1,99)=>', list1) #=insert(1,99)=> [10, 99, 20, 30, 40, 50]

print(list1.pop()) #마지막 항목 반환 및 삭제함수 #50
print('pop()=>', list1) #=pop()=> [10, 99, 20, 30, 40]

list1.remove(99) #지정삭제
print('remove(99)=>', list1) #=remove(99)=> [10, 20, 30, 40]

list1.reverse() #리스트 반전
print('reverse()=>', list1) #=reverse()=> [40, 30, 20, 10]

'''
List Comprehension
    : 대괄호 안에 for루프로 반복적인 표현식을 실행해서
    리스트 요소들을 초기화 하는 방법
    형식]
        [표현식 for 요소 in 컬렉션 [if조건식]]
'''
print("===List Comprehension", "="*30)
'''
    표현식(n의 제곱) 반복문(n값 0~9까지) 조건식(3의 배수)
        => n이 0~9까지 증가하면서 3의 배수인 경우에만 제곱값을 리스트에 초기화한다
        => 출력 값 : [0, 9, 36, 81]
'''
list = [n ** 2 for n in range(10) if n%3==0]
print(list)

