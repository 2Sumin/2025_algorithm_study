from collections import deque

def solution(priorities, location):

    queue = deque()
    cnt = 0

    for i in range(len(priorities)): # (우선순위, 위치)
        queue.append((priorities[i], i))

    while queue:
        current = queue.popleft()

        # 현재 프로세스보다 우선순위가 높은 프로세스가 큐에 있는지 확인
        flag_process_priority = False
        for i in queue:
            if i[0] > current[0]: # current 의 첫 원소 - popped priorities 
                flag_process_priority = True
                break

        # 우선순위가 더 높은 작업이 있으면 다시 큐에 넣음
        if flag_process_priority:
            queue.append(current)
        else :
            cnt += 1
            if current[1] == location: 
                return cnt
