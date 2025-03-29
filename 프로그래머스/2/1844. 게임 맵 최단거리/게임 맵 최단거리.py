from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    answer = bfs(maps, n, m)
    
    return answer

'''
도착을 위한 최소 칸 수 return
도착 불가 -> -1 return
1 <= n, m <= 100
'''

def bfs(maps, n, m):
    queue = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = set()
    visited.add((0, 0))
    queue.append((0, 0, 1))
    while queue:
        cur_x, cur_y, cnt = queue.popleft()
        
        if cur_x == n-1 and cur_y == m-1:
            return cnt
        
        for i in range(4):
            nx = dx[i] + cur_x
            ny = dy[i] + cur_y
            if nx < 0 or nx >= n or ny < 0 or ny >= m or (nx, ny) in visited or maps[nx][ny] == 0: continue
            queue.append((nx, ny, cnt+1))
            visited.add((nx, ny))
            
    return -1
    

