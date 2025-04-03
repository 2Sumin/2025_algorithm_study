def solution(num):
    
    # 주어진 수가 1이면 0 반환
    if num == 1:
        return 0
    
    cnt = 0  # 연산 횟수
    
    while num != 1:
        if num % 2 == 0:  # 짝수라면 2로 나누기
            num //= 2
        else:  # 홀수라면 3을 곱하고 1을 더하기
            num = num * 3 + 1
        
        cnt += 1  # 연산 횟수 증가
        
        if cnt >= 500:  # 500번 시도했는데도 1이 되지 않으면 -1 반환
            return -1
    
    return cnt
