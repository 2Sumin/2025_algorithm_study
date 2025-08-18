def solution(brown, yellow):
    
    # 약수 탐색 
    for h_in in range(1, int(yellow**0.5) + 1):
        if yellow % h_in == 0:
            w_in = yellow // h_in
            W, H = w_in + 2, h_in + 2
            if 2*W + 2*H - 4 == brown: # 갈색 수식이 맞는지 확인하고 리턴
                return [W, H]  
    
