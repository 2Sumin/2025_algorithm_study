def solution(sizes):
    max_big = 0
    max_small = 0
    
    for w, h in sizes:
        # 가로, 세로 -> 큰 값과 작은 값으로 나눠서 
        # 모든 명함의 큰 값들 중 최댓값 = 지갑의 한 변
        # 모든 명함의 작은 값들 중 최댓값 = 지갑의 다른 한 변
        big = max(w, h)
        small = min(w, h)
        max_big = max(max_big, big)
        max_small = max(max_small, small)
    
    return max_big * max_small
