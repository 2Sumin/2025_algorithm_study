def solution(n):
    answer = 0
    sum = 0
    # n이하의 수로 모두 나눠보고 0으로 나누어 떨어지면 더함. 
    
    for i in range (1, n+1):
        if n % i == 0:
            sum += i
    answer = sum
    return answer
