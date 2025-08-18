def solution(k, dungeons):
    # 유저의 현재 피로도 k
    # dungeons:["최소 필요 피로도", "소모 피로도"]
    # return : 유저가 탐험할 수 있는 최대 던전 수
    
    # DFS 
    
    n = len(dungeons)
    visited = [False] * n 
    answer = 0
    
    def dfs(energy, count): 
        nonlocal answer # 함수내부에서도 사용가능하도록
        answer = max(answer, count)
    
        for i in range(n):
            need, cost = dungeons[i]
            if not visited[i] and energy >= need: 
                visited[i] = True
                dfs (energy-cost, count + 1)
                visited[i] = False # 탐색 순서 변경 가능하도록 
    dfs(k,0)
    return answer
