from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    ## [반복문에 트럭 넣을 때 조건] ##
    # 다리 위 트럭의 수 ≤ bridge_length
    # 다리 위 트럭들의 무게 총합 + 새 트럭 무게 ≤ weight
    
    ## [트럭 뺄 때 조건] ##
    # 다리 위에서 bridge_length초 지난 트럭은 빠져야 함. 
    # 남은 거리 == 0 이면 맨 앞 트럭 제거 
    
    t = 0
    weight_cumm = 0 # 다리위의 시점별 무게
    out_truck = 0
    
    bridge = deque([0] * bridge_length) # 처음 다리 위(한대도 없는 상태)
    truck_weights = deque(truck_weights) # 꺼낼때 편하게 리스트 -> 큐 구조로 바꿔줌
    
    while weight_cumm or len(truck_weights) > 0 :
        t += 1
    
        out_truck = bridge.popleft()
        weight_cumm -= out_truck
        
        if truck_weights:
            if weight_cumm + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                weight_cumm += truck
            else :
                bridge.append(0) 
        
        
    return t
