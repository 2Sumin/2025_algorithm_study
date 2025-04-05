def solution(a, b):
        
    i = 0
    total = 0
    while i < len(a) :
        total += a[i] * b[i]
        i += 1
                   
    return total
