'''
모듈
    : 다른 파이썬 프로그램에서 불러와 사용할 수 있게 만든 파이썬
    파일로 함수나 변수 또는 클래스를 모아 놓은 것을 말한다.
    모듈을 모아 놓은 것을 패키지라고 한다.
    
    형식]
        import 모듈명
        from 모듈명 import 함수
'''

#모듈 사용방법1 : 함수 호출 시 모듈명을 같이 기술한다
import mod1
print("모듈의 함수호출1 :", mod1.add(3, 4))
print("모듈의 함수호출2 :", mod1.sub(4, 2))


#모듈 사용방법 2 : 특정함수까지 import하여, 함수 호출 시 모듈명을 생략한다.
from mod1 import add
result = add(3, 4)
print("결과:", result)
#resultSub = sub(3, 4) #sub함수는 import하지 않아 오류 발생
#print("결과:", resultSub)

#방법2와 동일하지만 모든 함수를 한번에 import한다
from mod1 import *
result1 = add(3, 4)
print("결과: ", result1)
result2 = sub(3, 4)
print("결과: ", result2)

'''
__name__변수를 저장한 모듈로 import를 하게되면 "mod2"가 저장되어 if문실행 안됨
'''
import mod2
result = mod2.mul(3, 4)
print(result)

#모듈을 나눠서 관리할때는 패키지를 사용하고
import kosmo.mod3
kosmo.mod3.sum1To10() #함수 호출시에는 패키지명까지 기술

# from절을 사용하여 함수를 import한 후 함수명만으로 호출 가능
from kosmo.mod3 import sum1To10 
sum1To10()