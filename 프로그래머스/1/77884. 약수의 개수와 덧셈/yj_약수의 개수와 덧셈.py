def solution(left, right):
     
    
    def count_divisors(n):
        cnt = 0 
        for i in range(1, n+1) :
            if (n % i == 0):
                cnt += 1
        return cnt
    
    
    sum1 = 0 
    sum2 = 0
    
    for i in range (left, right+1) :
        num = count_divisors(i)
        
        if num % 2 == 0:
            sum1 += i 
        else :
            sum2 += i 
    return sum1 - sum2
