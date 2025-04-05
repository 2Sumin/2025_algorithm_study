import math

def solution(left, right):
    # 어떤 수의 제곱이라면 약수의 수가 홀수
    ans = 0
    for i in range(left, right+1):
        if math.sqrt(i) == int(math.sqrt(i)):
            ans-=i
        else:
            ans+=i
    return ans