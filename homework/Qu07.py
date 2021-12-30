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
    for j in range(9):
        if j<4-i:
            print(' ', end='')
        elif j<5+i:
            print('*', end='')
    print()
    
    
'''
i   j            별출력조건
0  0~3       4        <5
1  0~2      4,5       <6
2  0~1     4,5,6      <7
3  0      4,5,6,7     <8
4        4,5,6,7,8    <9
   j<4-i             j<5+i    
'''

#SB
for i in range(5):
    for j in range(5):
        if(i+j>=4):
            print('*', end='')
            if(j+i>=5):
                print('*', end='')
        else:
            print(' ',end='')
    print()