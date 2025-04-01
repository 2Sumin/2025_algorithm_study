import math

def solution(progresses, speeds):
    ans = [] # 정답
    stack = []
    # 완성까지 남은 날의 수를 스택에 작성
    for i in range(len(progresses)-1, -1, -1):
        stack.append(math.ceil((100-progresses[i])/speeds[i]))
    # 스택이 전부 빌 때까지 반복
    # 스택의 top 요소를 제거하는데, 아래 요소 중 이전에 완성된 것이 있으면 pop
    while stack:
        cnt = 1
        current_day = stack[-1]
        stack.pop()
        while stack and stack[-1] <= current_day:
            stack.pop()
            cnt += 1
        ans.append(cnt)
    return ans