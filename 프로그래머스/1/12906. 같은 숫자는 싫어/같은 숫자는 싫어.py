def solution(arr):
    stack = [arr[0]]
    for i in arr:
        # stack의 top 원소와 다를 때만 append
        if stack[-1] != i:
            stack.append(i)
    return stack