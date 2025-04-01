def solution(n):

    # digits = list(map(int, str(n)))  
    digits = list(map(int,str(n)))
    s_digits = sorted(digits, reverse = True)

    # 배열을 문자열로 변환(map 사용),"".join 으로 문자열을 연결, 다시 int 변환 
    return int("".join(map(str,s_digits)))

