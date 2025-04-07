from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    ## [반복문에 트럭 넣을 때 조건] ##
    # 다리 위 트럭의 수 ≤ bridge_length
    # 다리 위 트럭들의 무게 총합 + 새 트럭 무게 ≤ weight
    
    ## [트럭 뺄 때 조건] ##
    # 다리 위에서 bridge_length초 지난 트럭은 빠져야 함. 
    # 남은 거리 == 0 이면 맨 앞 트럭 제거 
    
    t = 0 # 리턴값 : 다리 통과에 총 몇초 소요?
    weight_cumm = 0 # 다리위의 시점별 무게
    out_truck = 0
    
    bridge = deque([0] * bridge_length) # 처음 다리 위(한대도 없는 상태)
    truck_weights = deque(truck_weights) # 꺼낼 때 편하게 리스트 -> 큐 구조로 바꿔줌 (AI 도움)
    
    while weight_cumm or len(truck_weights) > 0 :
        t += 1 # 차가 들어올 때 1초 소요 
    
        out_truck = bridge.popleft()
        weight_cumm -= out_truck 
        
        if truck_weights: 
            if weight_cumm + truck_weights[0] <= weight: # 현재 다리 위 무게 + 새로운 트럭의 무게가 총 무게 한도 내이면
                truck = truck_weights.popleft()
                bridge.append(truck)
                weight_cumm += truck
            else : # 총 한도를 넘었으면 트럭말고 0 을 넣음 (시간의 흐름 반영)
                bridge.append(0) 
        
        
    return t
