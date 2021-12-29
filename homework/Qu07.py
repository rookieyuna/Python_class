'''
[문제 7]

아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
    *
   ***
  *****
 *******
*********

'''

for i in range(5):
    for j in range(10):
        if j<4-i:
            print(' ', end='')
        elif j<4-i+1+(2*i):
            print('*', end='')
    print()