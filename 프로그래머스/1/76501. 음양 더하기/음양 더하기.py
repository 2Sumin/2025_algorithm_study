def solution(absolutes, signs):
    ans = 0
    for i in range(len(absolutes)):
        num = absolutes[i]
        if not signs[i]:
            num *= -1
        ans += num
    return ans