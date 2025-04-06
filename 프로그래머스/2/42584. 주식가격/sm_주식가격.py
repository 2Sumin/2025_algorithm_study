def solution(prices):
    ans = [0] * len(prices)
    stack = []
    for day, price in enumerate(prices):
        # price(현재 가격)보다 높은 가격이 스택에 있으면 Pop
        while stack and stack[-1][1] > price:
            prev_day = stack.pop()[0] # 가격이 떨어진 시점의 인덱스
            ans[prev_day] = day-prev_day # 떨어지기까지 걸린 시간
        stack.append((day, price))
    # 가격이 떨어지지 않은 주식
    while stack:
        prev_day = stack.pop()[0]
        ans[prev_day] = len(prices)-1-prev_day
    return ans
