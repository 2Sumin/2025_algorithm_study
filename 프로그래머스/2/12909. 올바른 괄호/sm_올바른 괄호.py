def solution(s):
    stack = []
    for p in s:
        # 여는 괄호면 닫는 괄호 추가
        if p == '(':
            stack.append(')')
        # 닫는 괄호가 스택의 top에 있으면(닫는 괄호가 올 차례라면) 괄호 제거
        elif stack and stack[-1]==p:
            stack.pop()
        # 짝이 맞지 않으면(열린 괄호가 없는데 닫는 괄호가 들어오면) False
        else:
            return False
    # 스택이 비어있으면 True
    return not stack
