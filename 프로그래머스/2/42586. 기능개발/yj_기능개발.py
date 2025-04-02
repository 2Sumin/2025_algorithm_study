# 너굴맨 - 시간복잡도 질문
from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    
    # 큐 
    # 남은 일수 구하기
    # 100 - progresses / speeds = 남은 일수 
    # 남은 일수는 차례대로 큐에 넣음
    
    queue = deque() # 큐 선언
    
    # 각 작업이 완료되는 날짜 -> 큐에 저장
    for p, s in zip(progresses, speeds):
        queue.append(math.ceil((100 - p) / s))  
        
    while queue : # O(n)
        
        cnt = 1 # cnt = 배포될 기능 수
        d = queue.popleft() # 아래 반복문에서 사용
        
        while queue and queue[0] <= d : # O(n) + O(n)
            queue.popleft() # 같이 배포된 후 큐에서 완전 제거
            cnt += 1
        
        answer.append(cnt)
        

    return answer
