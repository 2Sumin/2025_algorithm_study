

def solution(participant, completion): 
    from collections import defaultdict # 기본값이 0인 딕셔너리
    
    cnt = defaultdict(int)
    for i in participant: 
        cnt[i] += 1 
        
    for j in completion: 
        cnt[j] -= 1 # 위에서 
        
    for name, c in cnt.items():
        if c > 0:
            return name
