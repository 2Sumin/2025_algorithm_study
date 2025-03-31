def solution(n):
    cnt = 0
    k=1
    
    # 주어진 자연수가 짝수일 경우 -> 0개 (연속된 자연수는 홀짝의 구성이기 때문)
    #if(n%2 == 0)
    #return 0
    
    # 주어진 자연수가 홀수일 경우 
    #else
    while k * (k-1) // 2 < n: # 보다 작아야 함. 
        if(n-k*(k-1)//2)%k ==0:
            cnt+=1
        k+=1
    
    
    return cnt
