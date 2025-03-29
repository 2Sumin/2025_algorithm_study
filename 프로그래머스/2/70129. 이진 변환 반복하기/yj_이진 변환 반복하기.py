def solution(s):
    # answer = []
    cnt_zero = 0
    cnt_bin = 0
    # 이진 변환의 횟수
    # 변환 과정에서 제거된 모든 0의 개수

    while s != "1":

        # 문자열에서 0 제거 
        num_zeros = s.count("0")
        cnt_zero += num_zeros
        s = s.replace("0","")

        # 문자열의 길이 세기 (길이 = n) 
        n = len(s)
        # n을(십진수) 이진수로 변환 (접두어 제거)
        s = bin(n)[2:]

        cnt_bin += 1 # 이진 변환의 횟수 세기


    return [ cnt_bin, cnt_zero]
