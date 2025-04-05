def solution(prices):
    
    stack = []
    seconds = 0
    answer = [0] * len(prices)
    
    for p in range(len(prices)):
        
        while stack and prices[p] < stack[-1][1]:
            idx, price = stack.pop()
            answer[idx] = p - idx # 몇 초 동안 상승상태였는지 
            
        stack.append((p ,prices[p]))
        
        for idx, price in stack: # 스택에 남은 가격들 처리 
            answer[idx] = len(prices) - idx - 1
    
    return answer
