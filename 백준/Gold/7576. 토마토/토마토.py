import sys
from collections import deque

inp = sys.stdin.readline
m, n = map(int, inp().split()) #y, x
matrix = [list(map(int, inp().strip().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()
cur = [0]*3
res = 0
zero = 0
cnt = 0

for i in range(n):
    zero += matrix[i].count(0)

if zero == 0:
    print(0)
    exit()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j, 0])
            matrix[i][j] = 2
while queue:
    cur = queue.popleft()
    for k in range (4):
        nx = cur[0] + dx[k]
        ny = cur[1] + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or matrix[nx][ny]==-1: continue
        if matrix[nx][ny] == 0:
            matrix[nx][ny] = 2
            queue.append([nx, ny, cur[2]+1])
            cnt += 1
res+=cur[2]
if zero == cnt:
    print(res)
    exit()
else:
    print(-1)
    exit()