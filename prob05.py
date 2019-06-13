# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

def mysum(*num):
    result = 0
    for i in num:
        result += i

    print(result)

mysum(1, 5, 9)