def solution(num):
    
    # 2로 나누어서 = 0 -> 짝
    # = 1 -> 홀
    return "Even" if num % 2 == 0 else "Odd"
