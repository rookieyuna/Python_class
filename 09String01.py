'''
06String - f-String (파이썬 버전 3.6 부터 사용)
    형식]
        f'문자열{변수}문자열'
        f'문자열{리스트명[n]}문자열'
        f'문자열{dics["key"]}문자열'
    정렬형식]
        '{문자열:<길이}'
                <: 좌측정렬
                >: 우측정렬
                ^: 센터정렬
                남은 칸은 공백으로 채움
'''

#문자열 앞에 f를 쓰고, 표현할 변수를 중괄호를 이용해서 삽입한다
str = 'coffee'
num = 1
result = f'{str}는 하루에 {num}잔만 마시는게 좋아요'
print(result)

#정해진 공간에서의 정렬 (|은 서식아님! 단순히 공간확인용)
s1 = '좌측정렬'
result1 = f'|{s1:<10}|'
print(result1) #=|좌측정렬      |

s2 = '중앙정렬'
result2 = f'|{s2:^10}|'
print(result2) #=|   중앙정렬   |

s3 = '우측정렬'
result3 = f'|{s3:>10}|'
print(result3) #=|      우측정렬|

# f-String에 딕셔너리를 사용 : key값을 사용해서 변수 출력
dics = {'name':'루키', 'gender':'수컷', 'age':'7'}
result = f'{dics["name"]}는 {dics["gender"]}이고 나이는 {dics["age"]}살이다'
print(result)

#리스트를 사용 : 배열처럼 index를 사용해서 변수 출력
lists = [10,20,30]
print(f'리스트 : {lists[0]}, {lists[1]}, {lists[2]}')
for v in lists:
    print(f'반복출력 : {v}')