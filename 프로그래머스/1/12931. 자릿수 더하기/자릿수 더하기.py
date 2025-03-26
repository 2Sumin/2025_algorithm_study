def solution(n):
    ans = 0
    while n>0:
        # 마지막 자릿수 더하기
        ans += n%10
        n//=10
    return ans