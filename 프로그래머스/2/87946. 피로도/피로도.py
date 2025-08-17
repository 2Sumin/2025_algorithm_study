from itertools import permutations

def solution(k, dungeons):
    n = len(dungeons)
    max_cnt = 0
    
    # 모든 던전 순서 생성
    for order in permutations(dungeons, n):
        energy = k  # 현재 피로도
        cnt = 0     # 탐험한 던전 수
        
        for min_need, cost in order:
            # 입장 가능하면 던전 돌고 피로도 감소
            if energy >= min_need:
                energy -= cost
                cnt += 1
            # 더 이상 못 돌면 중단
            else:
                break
        max_cnt = max(max_cnt, cnt)
                
    return max_cnt