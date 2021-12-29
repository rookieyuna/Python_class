'''
파일명 : 03Tuple.py

파이썬에는 연속된 Collection 데이터 구조에
list, tuple, dictionary, set 이 있다.

튜플(Tuple)
    : 소괄호() 안에 콤마로 구분된 항목들이 나열되어 표현되는 시퀀스 자료형
    서로 다른 자료형으로 구성할 수 있지만, 대입연산자로 튜플의 항목을 변경할 수 없다
    - 인덱싱, 슬라이싱, 연결, 반복이 가능하다
    - Immutable 데이터 타입이라고 한다
'''

tu1 = tuple() #빈 튜플 생성
tu2 = (1,2,3,4,5)
tu3 = 1, #1개의 항목을 갖는 튜플 생성. 콤마가 없으면 단순한 변수선언이 됨
tu4 = (98, 99, 100)
print(tu1, tu2, tu3) #=() (1, 2, 3, 4, 5) (1,)

print("===인덱싱/슬라이싱", "="*30)
print("tu2[0]:", tu2[0]) #=1
print("tu2[-1]:", tu2[-1]) #=5 #인덱스가음수인경우 마지막항목출력 
print("tu2[-2]:", tu2[-2]) #=4
print("tu2[1:3]:", tu2[1:3]) #=(2, 3)

#해당요소가 포함되었는지 확인
print("==포함여부확인", "="*30)
print("4 in tu2:", 4 in tu2) #=True
print("99 not in tu2:", 99 not in tu2) #=True

print("===반복출력", "="*30)
print("tu2 * 3:", tu2 * 3) #=(1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

print("===병합", "="*30)
new_tu = tu2 + tu4
print("new_tu", new_tu) #=(1, 2, 3, 4, 5, 98, 99, 100)
all_tuple = [tu2, tu4]
print('all_tuple:', all_tuple)#=all_tuple: [(1, 2, 3, 4, 5), (98, 99, 100)]

#튜플과 리스트간의 변환을 위한함수
print("===튜플과 리스트 변환", "="*30)
my_list = [1,2,3]
my_tuple = ('x', 'y', 'z')
print(tuple(my_list)) #=(1, 2, 3)
print(list(my_tuple)) #=['x', 'y', 'z']