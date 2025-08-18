def solution(sizes):
    
    # 주어진 명함 -> [짧은,긴] 으로 정렬 
    # 짧은 중 max * 긴 중 가장 max
    
    max_short = max_long = 0
    
    for w,h in sizes: 
        short, long = min(w,h), max(w,h)
        max_short = max(short, max_short)
        max_long = max(long, max_long)
        
        
    return max_short * max_long
