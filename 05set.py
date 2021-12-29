'''
파일명 : 05set.py

파이썬에는 연속된 Collection 데이터 구조에
list, tuple, dictionary, set 이 있다.

집합/셋(Set)
    : 객체를 참조하기 위한 순서가 없는 Collection 자료형
    딕셔너리처럼 중괄호{}로 선언하지만 key값은 없다.
    값이 중복되면 한 개의 값만 등록되며 값은 변경할 수 있다.
    - Mutable 데이터 타입이다
'''
#set()함수를 통해 새로운 set을 생성한다.
empty_set = set()
print(empty_set)

#set()함수의 인자로 리스트를 전달하여 set으로 변환한다.
even_set = set([0,2,4,6,8])
print(even_set) #={0, 2, 4, 6, 8}

#생성과 동시에 초기화. 중복값은 제거된다.
odd_set = {1,3,5,7,9,7,5,3,1}
print(odd_set) #={1, 3, 5, 7, 9}


#새로운 set 초기화
myset = {1,3,5}

#add() : 인자추가함수
myset.add(7)
print("myset1=", myset) #= {1, 3, 5, 7}
#update() : 다수의 인자 추가 함수
myset.update({4,6,8})
print("myset2=", myset) #= {1, 3, 4, 5, 6, 7, 8}
#remove() : 삭제함수. 단 여러개 삭제 불가
myset.remove(1)
print("myset3=", myset) #= {3, 4, 5, 6, 7, 8}
#clear() : 전체삭제 함수
myset.clear()
print("myset4=", myset) #= set()

#집합연산
set_a = {1,3,5,7,9}
set_b = {1,2,5}
print("합집합", set_a | set_b) #= {1, 2, 3, 5, 7, 9}
print("교집합", set_a & set_b) #= {1, 5}
print("차집합", set_a - set_b) #= {9, 3, 7}