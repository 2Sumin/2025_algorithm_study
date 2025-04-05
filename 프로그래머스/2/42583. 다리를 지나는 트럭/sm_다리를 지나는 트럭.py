from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리를 큐로 표현
    current_weight = 0  # 현재 다리 위의 트럭 무게 합
    truck_weights = deque(truck_weights)  # 대기 트럭 목록도 큐로 변환
    
    # 모든 트럭이 다리를 건너갈 때까지 반복
    while bridge:
        time += 1
        # 다리의 맨 앞에서 트럭이 나옴 
        current_weight -= bridge.popleft()
        
        # 대기 중인 트럭이 있다면
        if truck_weights:
            # 다음 트럭이 다리에 올라갈 수 있는지 확인
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                # 트럭이 올라갈 수 없으면 0을 추가 (빈 공간)
                bridge.append(0)
        
    return time
