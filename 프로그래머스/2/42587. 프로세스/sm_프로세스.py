from collections import deque

def solution(priorities, location):
    q = deque()
    num = 0
    for idx, pri in enumerate(priorities):
        q.append((idx, pri))

    while q:
        idx, pri = q.popleft()

        # 우선순위가 더 높은 게 있으면 다시 넣기
        if any(pri < other_pri for _, other_pri in q):
            q.append((idx, pri))
        # 실행
        else:
            num += 1

            if idx == location:
                return num
