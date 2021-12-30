'''
06String - 다양한 문자열 함수 참고(수업외 교안)
'''

'''
#capitalize()
 : 첫 문자가 대문자이고 나머지가 소문자인 문자열의 복사본을 리턴한다.
'''
a = 'PYTHON'
print( a.capitalize() ) #=Python


'''
#count(x, start, end)
 :  인자 x의 갯수를 카운트하여 리턴한다.
    x - 개수를 찾을 문자열 또는 문자
    start(선택) - 검색이 시작되는 문자열 내에서 시작 색인.
    end(선택) - 검색이 끝나는 문자열 내에서 끝 인덱스.
'''
a = 'pythonpp'
print(a.count('p')) #=3 
a = 'pythonpy'
print(a.count('py',0,5)) #=1


'''
find(sub, start, end)
 : 문자열 내에서 특정문자열을 찾아 인덱스를 반환한다.
    찾는 문자나 문자열이 없을시 -1 을 반환한다.
    sub - 검색 할 문자열
    start(선택) - 검색이 시작되는 문자열 내에서 시작 색인.
    end(선택) - 검색이 끝나는 문자열 내에서 끝 인덱스.
'''
a = 'pythonpy' 
print(a.find('y')) #=1
print(a.find('py',0,5)) #=0
print(a.find('tk')) #=-1


'''
index(sub, start, end)
 : 문자열 내에서  특정문자열의 인덱스를 찾아 반환. 찾는문자(열)이 없으면 오류가 발생.
    sub - 검색 할 문자열
    start(선택) - 검색이 시작되는 문자열 내에서 시작 색인.
    end(선택) - 검색이 끝나는 문자열 내에서 끝 인덱스.
'''