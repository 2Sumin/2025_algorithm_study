def solution(x, n):
    
    answer = []
    cur = x
    
    for _ in range(n): 
        answer.append(cur)
        cur += x
    
    return answer
