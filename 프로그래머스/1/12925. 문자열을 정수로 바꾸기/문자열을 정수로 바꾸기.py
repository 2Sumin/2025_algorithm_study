def solution(s):
    # 음수
    if s[0] == '-': 
        return -1 * int(s[1:])
    # 양수
    else: 
        if s[0] == '+':
            return int(s[1:])
        else:
            return int(s)
    