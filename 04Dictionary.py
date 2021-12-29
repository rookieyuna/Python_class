'''
파일명 : 04Dictionary.py

파이썬에는 연속된 Collection 데이터 구조에
list, tuple, dictionary, set 이 있다.

사전/딕셔너리(Dictionary)
    : 고유키(key)를 이용하여 값(value)을 저장하는 자료형. 
    콜론(:)으로 구분하며 자료의 순서는 의미가 없다
    값은 변경할 수 있고 중괄호{}로 선언한다.
    - Mutable 데이터 타입이다
'''

#생성1 : dict()함수를 이용해서 딕셔너리 생성
dic1 = dict(birth=1970, name="홍길동", size="100cm")
print(dic1)

#생성2: 중괄호를 이용한 생성
dic2 = {'one':1, 'two':2, 'three':3}   
print(dic2) #={'one': 1, 'two': 2, 'three': 3}

#반복문을 이용한 딕셔너리 출력
fruits = {'apple':100, 'grapes':200, 'orange':300, 'peach':400}
print('for문을 이용한 출력')
for key in fruits:
    val = fruits[key] #key를 먼저 얻어온 후,
    print("%s : %d" % (key, val)) #얻어온 key를 통해 value를 출력한다.
'''
apple : 100
grapes : 200
orange : 300
peach : 400
'''

#딕셔너리의 크기(길이)
print("길이", len(fruits)) #=길이 4
print("복숭아", fruits['peach'])

#이미 있는 key에 값 입력시 값이 변경됨
fruits['orange'] = 3500
print("오렌지", fruits['orange']) #=오렌지 3500

#key에 해당하는 값을 삭제한다
del fruits['peach']
print('fruits=', fruits)

#keys() : 딕셔너리의 키로된 dict_keys 객체를 반환한다
get_keys = fruits.keys()
for k in get_keys: 
    print(k) #key를 출력한다
    
#values() : 딕셔너리의 값들로된 dict_values 객체를 반환한다
get_values = fruits.values()
for v in get_values:
    print(v) #value를 출력한다