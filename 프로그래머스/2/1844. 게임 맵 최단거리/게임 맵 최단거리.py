from collections import deque

def solution(maps):
    # 최단거리 -> bfs    
    row_len = len(maps)
    col_len = len(maps[0])
    
    if (maps[0][0] == 0 or maps[row_len-1][col_len-1] == 0):
        return -1
    
    visited = [[False]*col_len for _ in range(row_len)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    q = deque()
    q.append((0,0))
    maps[0][0] = 1
    
    while q:
        cur_r, cur_c = q.popleft()
        if cur_r == row_len-1 and cur_c == col_len-1:
            return maps[cur_r][cur_c]
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if (0<=next_r<row_len and 0<=next_c<col_len):
                if maps[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    q.append((next_r, next_c))
                    maps[next_r][next_c] = maps[cur_r][cur_c] + 1
    
    return -1   