from collections import deque
def bfs(maps):
    
    # 방향 벡터
    #     동, 서, 남, 북
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    n = len(maps)
    m = len(maps[0])

    # -------------------------------
    
    visited = [[False] * m for _ in range(n)]
    distance = [[0] * m for _ in range(n)]
    
    visited[0][0] = True
    distance[0][0] = 1
    
    q = deque()
    q.append((0,0)) # 시작점
    
    # --------------------------------
        
    while q:
        x, y = q.popleft()
            
        for i in range(4): # 4방향 이동
            nx = x + dx[i]
            ny = y + dy[i]
                
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
        
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx,ny))
                
                
    return distance[n-1][m-1] if visited[n-1][m-1] else -1
    
def solution(maps):
    
    # 최단거리 구하기 -> bfs
    return bfs(maps)
