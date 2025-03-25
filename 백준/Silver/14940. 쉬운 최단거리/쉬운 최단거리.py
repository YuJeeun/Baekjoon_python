import sys
from collections import deque
inp = sys.stdin.readline

n, m = map(int, inp().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = [list(map(int, inp().split())) for _ in range(n)]
result = []
cnt = 0
queue = deque()

for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                end_x, end_y = i, j
                break
def bfs():
    visit = [[False]*m for _ in range(n)]
    distance = [[-1]*m for _ in range(n)]
    queue.append((end_x, end_y))
    visit[end_x][end_y] = True
    distance[end_x][end_y] = 0

    while queue:
        cur_x, cur_y = queue.popleft()

        for k in range(4):
            nx = dx[k] + cur_x
            ny = dy[k] + cur_y
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visit[nx][ny] or arr[nx][ny] == 0: continue
            queue.append((nx, ny))
            distance[nx][ny] = distance[cur_x][cur_y] + 1
            visit[nx][ny] = True

    result = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                result.append(distance[i][j])
            elif arr[i][j] == 0 or arr[i][j] == 2:
                result.append(0)
    cnt = 0
    for r in result:
        print(r, end=' ')
        cnt += 1
        if cnt == m:
            print()
            cnt = 0

bfs()


