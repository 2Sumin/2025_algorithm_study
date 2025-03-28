def solution(s):
    cnt = 0
    zeros = 0 # 0의 개수
    while s!='1':
        # 1 개수 세기
        one_cnt = s.count('1')
        zeros += len(s) - one_cnt
        s = str(bin(one_cnt)[2:])
        cnt+=1   
    return [cnt, zeros]
