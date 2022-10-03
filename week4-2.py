# 숫자 찾기 게임

import os # 화면 지워야 하므로
import random as r # 랜덤한 자리에 8 넣어야 하므로
import time as t # 2초 동안 보여주고 사라지게 해야 하므로

eight = [0] * 40
victory = 0 # 맞춘 횟수

for i in range(5): # 총 5번 실행
    eight_index = r.randrange(40)
    eight[eight_index] = 8

    for j in range(40):
        print('%2d ' % j, end='') # index 0 ~ 39 출력
    
    print()

    for j in range(40):
        print(' %d ' % eight[j], end='') # eight 값 출력
    
    print()

    t.sleep(2)
    os.system('cls')

    user = int(input('8은 어디에? (인덱스 입력): '))

    if user == eight_index:
        victory += 1
        print('%d번 맞췄음' % victory)
    else:
        print('틀렸음, 맞춘 횟수 = %d' % victory)

    eight[eight_index] = 0

input()