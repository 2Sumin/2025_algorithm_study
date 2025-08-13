import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while len(scoville) > 1 and scoville[0] < K:
        cnt += 1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1+min2*2)
    
    return cnt if scoville[0]>=K else -1