from collections import deque
def solution(arr):

    queue = deque()  # 빈 큐 선언
    queue.append(arr[0]) 

    for i in range(1,len(arr)):
        if (arr[i-1] != arr [i]):                
            queue.append(arr[i]) 

    return list(queue)
