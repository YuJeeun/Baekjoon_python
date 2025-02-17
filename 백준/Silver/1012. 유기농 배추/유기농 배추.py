import sys
from collections import deque

inp = sys.stdin.readline

t = int(inp())
for _ in range(t):
    m, n, k = map(int, inp().split())
    land = [[0]*n for _ in range(m)]
    xy = [list(map(int, inp().split())) for _ in range(k)]
    
    for i in range(k):
        land[xy[i][0]][xy[i][1]] = 1

    queue = deque()
    cur = [0]*2

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0
    
    for i in range(m):
        for j in range(n):
            if land[i][j] == 1:
                land[i][j] == -1
                queue.append((i, j))
                while queue:
                    cur = queue.popleft()
                    for k in range(4):
                        nx = dx[k] + cur[0]
                        ny = dy[k] + cur[1]
                        if nx < 0 or ny < 0 or nx >= m or ny >= n or land[nx][ny] != 1: continue
                        land[nx][ny] = -1
                        queue.append((nx, ny))
                cnt += 1
    print(cnt)
