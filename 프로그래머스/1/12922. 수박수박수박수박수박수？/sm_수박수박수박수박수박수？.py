def solution(n):
    ans = ''
    # '수박'을 n//2번만큼 반복
    ans += '수박'*(n//2)
    if n%2==1:
        ans+='수'
    return ans
