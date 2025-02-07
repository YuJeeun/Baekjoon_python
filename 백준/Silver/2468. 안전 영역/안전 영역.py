import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp())

area = [list(map(int, inp().split())) for _ in range(n)]

queue = deque()
cur = [0]*2
visit = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
h = 0
max_h = 100

res = []
while h <= max_h:
    safe_area = 0
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] > h and visit[i][j]==0:
                queue.append([i, j])
                visit[i][j] = 1
                while queue:
                    cur = queue.popleft()
                    for k in range(4):
                        nx = dx[k] + cur[0]
                        ny = dy[k] + cur[1]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny] == 1 or area[nx][ny] <= h: continue
                        visit[nx][ny] = 1
                        queue.append([nx, ny])
                safe_area += 1
    res.append(safe_area)
    h += 1
print(max(res))


