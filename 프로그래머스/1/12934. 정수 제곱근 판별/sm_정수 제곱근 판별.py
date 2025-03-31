import math
def solution(n):
    # n의 제곱근 x가 정수인지 확인
    x = math.sqrt(n)
    if x == int(x):
        return pow(x+1,2)
    else:
        return -1
