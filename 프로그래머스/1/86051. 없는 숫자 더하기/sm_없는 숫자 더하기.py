def solution(numbers):
    ans = 0
    numbers.sort()
    for i in range(0,10):
        if i not in numbers:
             ans += i
    return ans
