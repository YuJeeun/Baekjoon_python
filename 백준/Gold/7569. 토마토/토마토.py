import sys
from collections import deque

inp = sys.stdin.readline

# y, x, z
m, n, h = map(int, inp().split())

grid = []

for i in range(h):
    tomato = []
    for k in range(n):
        tomato.append(list(map(int, inp().split())))
    grid.append(tomato)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dz = [1, -1] #위, 아래

queue = deque()
cur = [0]*4
d = 0

zero = [0]*2
for i in range(h):
    for j in range(n):
        zero[0] += grid[i][j].count(0)

if zero[0] == 0:
    print(0)
    exit()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if grid[i][j][k] == 1:
                queue.append([i, j, k, d])
                grid[i][j][k] = 2
while queue:
    cur = queue.popleft()
    for i in range(2):
        nz = cur[0] + dz[i]
        if nz < 0 or nz >= h or grid[nz][cur[1]][cur[2]] != 0: continue
        grid[nz][cur[1]][cur[2]] = 2
        queue.append([nz,cur[1],cur[2],cur[3]+1])
    for j in range(4):
        nx = cur[1] + dx[j]
        ny = cur[2] + dy[j]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or grid[cur[0]][nx][ny] != 0: continue
        grid[cur[0]][nx][ny] = 2
        queue.append([cur[0],nx,ny,cur[3]+1])

for i in range(h):
    for j in range(n):
        zero[1] += grid[i][j].count(0)

if zero[1]!=0: 
    print(-1) 
    exit()

print(cur[3])
