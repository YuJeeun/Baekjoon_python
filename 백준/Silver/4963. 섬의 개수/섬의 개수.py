import sys
from collections import deque
inp = sys.stdin.readline

queue = deque()

cur = [0]*2

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]

res = []
while True:
    w, h = map(int, inp().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, inp().split())) for _ in range(h)]
    visit = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0 and arr[i][j] == 1:
                queue.append([i, j])
                visit[i][j] = 1
                while queue:
                    cur = queue.popleft()
                    for k in range(8):
                        nx = dx[k] + cur[0]
                        ny = dy[k] + cur[1]
                        if nx < 0 or ny < 0 or nx >= h or ny >= w or visit[nx][ny] == 1 or arr[nx][ny] == 0: continue
                        visit[nx][ny] = 1
                        queue.append([nx, ny])
                cnt += 1
    res.append(cnt)

for i in res:
    print(i)