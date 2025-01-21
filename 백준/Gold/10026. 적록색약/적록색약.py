import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp())

grid = [[0]*n for _ in range(n)]
visit = [[0]*n for _ in range(n)]

for i in range(n):
    rgb = inp()
    for j in range(n):
        grid[i][j] = rgb[j]

queue = deque()
cur = [0]*2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result1 = 0
result2 = 0
for i in range (n):
    for j in range(n):
        if visit[i][j] == 0:
            queue.append([i, j])
            while queue:
                cur = queue.popleft()
                visit[cur[0]][cur[1]] = 1
                for k in range (4):
                    nx = cur[0] + dx[k]
                    ny = cur[1] + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or grid[nx][ny] != grid[cur[0]][cur[1]]: continue
                    if visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        queue.append([nx, ny])
            result1 += 1
print(result1, end=' ')

visit = [[0]*n for _ in range(n)]

for i in range (n):
    for j in range(n):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

for i in range (n):
    for j in range(n):
        if visit[i][j] == 0:
            queue.append([i, j])
            while queue:
                cur = queue.popleft()
                visit[cur[0]][cur[1]] = 1
                for k in range (4):
                    nx = cur[0] + dx[k]
                    ny = cur[1] + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or grid[nx][ny] != grid[cur[0]][cur[1]]: continue
                    if visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        queue.append([nx, ny])
            result2 += 1
print(result2)



