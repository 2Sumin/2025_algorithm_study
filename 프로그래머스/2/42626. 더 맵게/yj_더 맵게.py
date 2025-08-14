import heapq 
def solution(scoville, K):
    
    heapq.heapify(scoville)
    count = 0 
    
    # min-heap
    while len(scoville) > 1:
        
        # pop 결과가 K 이상이면 힙 내의 모든 원소가 K 이상
        f = heapq.heappop(scoville)
        if f >= K:
            return count
            
        # 아닐때는 수식 계산하여 값 update
        ff = heapq.heappop(scoville)
        value = f + (f*2)
        heapq.heappush(scoville,value)
        count += 1
    
    
    return count if scoville[0] >= K else -1
