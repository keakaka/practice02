# 문제6
# 숨겨진 카드의 수를 맞추는 게임입니다.
# 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다.
# 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면
# "더 높게", 다시 75이라고 입력하면 "더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다.
# 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.

import random, sys

num = random.randrange(100) + 1
print('수를 결정하였습니다. 맞춰보세요 \n1-100')
count = 1

while True:
    check = input((str(count) + '>> '))
    count += 1
    if check.isdigit():
        check = int(check)
        if num > check:
            print('더 높게')
            continue
        elif num < check:
            print('더 낮게')
            continue
        else:
            print('맞았습니다.')
            retry = input('다시 하시겠습니까? (Y/N) ').upper()
            if retry == 'N':
                sys.exit(0)
            elif retry == 'Y':
                count = 1
                num = random.randrange(100) + 1
                continue
            else:
                print('잘못 입력하셨습니다. 게임을 종료합니다.')
                sys.exit(0)
    else:
        print('숫자만 입력하세요')
        continue
