import sys
from collections import deque
inp = sys.stdin.readline

n = int(inp())

area = [list(map(int, inp().split())) for _ in range(n)]

maxx = max(area[0])
minn = min(area[0])
for i in range(1, len(area)):
    maxx = max(maxx, max(area[i]))
    minn = min(minn, min(area[i]))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()
res= []
for i in range(minn-1, maxx+1):
    cnt = 0
    visit = [[False]*n for _ in range(n)]   
    for j in range(n):
        for k in range(n):
            if area[j][k] > i and not visit[j][k]:
                visit[j][k] = True
                queue.append((j, k))
                while queue:
                    cur_x, cur_y = queue.popleft()
                    for l in range(4):
                        nx = cur_x + dx[l]
                        ny = cur_y + dy[l]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny] or area[nx][ny] <= i: continue
                        visit[nx][ny] = True
                        queue.append((nx, ny))
                cnt += 1
    res.append(cnt)

print(max(res))
