def solution(x):
    
    ## 하샤드 수 판별하기 ##
    
    # 각 자릿수의 합 구하기 
    sum_x = sum(int (num) for num in str(x))
    if x % sum_x == 0 :
        return True
    else : 
        return False
