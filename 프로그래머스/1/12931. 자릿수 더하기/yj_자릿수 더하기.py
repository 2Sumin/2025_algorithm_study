def solution(n):

    #1 
    # 문자열로 바꿔서 각 자리를 리스트에 담아서 -> 숫자 변환, 더하기
    # return sum(map(int, str(n)))

    #2 
    answer = 0
    while n > 0:
        answer += n % 10  # 1의 자리 숫자 더하기
        n //= 10  # 1의 자리 제거 (n을 10으로 나눈 몫을 다시 n에 저장)
    return answer
