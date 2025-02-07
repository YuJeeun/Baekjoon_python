import sys
from collections import deque

inp = sys.stdin.readline

n, m = map(int, inp().split())

lab = [list(map(int, inp().split())) for _ in range(n)]

visit = [[0]*m for _ in range(n)]

empty_area = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty_area.append([i, j])

wall = []

queue = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cur = [0]*2

res = 0

def build_wall(idx):
    if len(wall) == 3:
        bfs()
        return
    
    for i in range(idx, len(empty_area)):
        wall.append([empty_area[i][0], empty_area[i][1]])
        lab[empty_area[i][0]][empty_area[i][1]] = 1
        build_wall(i+1)
        wall.pop()
        lab[empty_area[i][0]][empty_area[i][1]] = 0

def bfs():
    global res
    tmp_res = 0
    visit = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0 and lab[i][j] == 2:
                queue.append([i, j])
                visit[i][j] = 1
                while queue:
                    cur = queue.popleft()
                    for k in range(4):
                        nx = dx[k] + cur[0]
                        ny = dy[k] + cur[1]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] == 1 or lab[nx][ny] == 1: continue
                        visit[nx][ny] = 1
                        queue.append([nx, ny])
    
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0 and lab[i][j] == 0:
                tmp_res += 1
    res = max(res, tmp_res)

build_wall(0)
print(res)

