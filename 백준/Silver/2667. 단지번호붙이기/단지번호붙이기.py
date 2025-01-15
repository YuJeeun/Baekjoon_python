import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp())
c = [inp().strip() for _ in range(n)]
matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(c[i][j])

queue = deque()
cur = [0]*3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            queue.append([i, j])
            matrix[i][j] = -1
            cnt = 1
            while len(queue) != 0:
                cur = queue.popleft()
                for k in range(4):
                    nx = cur[0] + dx[k]
                    ny = cur[1] + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or matrix[nx][ny]==0: continue
                    if matrix[nx][ny] == 1:
                        cnt += 1
                        queue.append([nx, ny])
                        matrix[nx][ny] = -1
            res.append(cnt)
print(len(res))
res.sort()
for i in range(len(res)):
    print(res[i])   
