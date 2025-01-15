import sys
from collections import deque
inp = sys.stdin.readline

t = int(inp())
cnt = 0
queue = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cur = [0]*2
res = []
while cnt<t:
    bug = 0
    m, n, k = map(int, inp().split())
    matrix = [[0]*m for _ in range(n)]
    c = [list(map(int, inp().split())) for _ in range(k)]
    cnt+=1
    for i in range(k):
        matrix[c[i][1]][c[i][0]] = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                queue.append([i, j])
                matrix[i][j] = 2
                while len(queue) != 0:
                    cur = queue.popleft()
                    for k in range(4):
                        nx = cur[0] + dx[k]
                        ny = cur[1] + dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m or matrix[nx][ny] == 0: continue
                        if matrix[nx][ny] == 1:
                            matrix[nx][ny] = 2
                            queue.append([nx, ny])
                bug += 1
                
    res.append(bug)

for i in range(t):
    print(res[i])