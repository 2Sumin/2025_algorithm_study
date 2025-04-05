def solution(a, b):
    return sum(x*y for x,y in zip(a,b))
    # ans = 0
    # for i in range(len(a)):
    #     ans += a[i]*b[i]
    # return ans
