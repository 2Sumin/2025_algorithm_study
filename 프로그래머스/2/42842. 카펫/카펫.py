def solution(brown, yellow):
    total = brown + yellow
    
    # 가로(width)와 세로(height) 모든 조합을 확인
    # 최소 크기: 3x3 (테두리 1줄 + 노란색 최소 1x1)
    for width in range(3, total + 1):        # 가로: 3부터 total까지
        for height in range(3, width + 1):   # 세로: 3부터 가로까지
            
            # 1. 전체 격자 수 확인
            if width * height == total:
                
                # 2. 노란색 격자 수 확인
                # 노란색 격자 수 = (가로-2) × (세로-2) 
                # (테두리 1줄씩 제외한 안쪽 부분)
                yellow_area = (width - 2) * (height - 2)
                
                if yellow_area == yellow:
                    # 3. 갈색 격자 수 확인
                    brown_area = total - yellow_area
                    
                    if brown_area == brown:
                        return [width, height]