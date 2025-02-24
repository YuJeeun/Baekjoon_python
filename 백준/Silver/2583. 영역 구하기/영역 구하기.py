import sys
from collections import deque
inp = sys.stdin.readline

m, n, k = map(int, inp().split())

coordinate = [list(map(int, inp().split())) for _ in range(k)]

board = [[0]*n for _ in range(m)]

for i in range(len(coordinate)):
    for j in range(coordinate[i][0], coordinate[i][2]):
        for k in range(coordinate[i][1], coordinate[i][3]):
            board[k][j] = 1

queue = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = []
area = 0
for i in range(m):     
    for j in range(n): 
        if board[i][j] == 0:
            area += 1
            cnt = 1
            queue.append((i, j))
            board[i][j] = -1
            while queue:
                cur_x, cur_y = queue.popleft()
                for k in range(4):
                    nx = dx[k] + cur_x
                    ny = dy[k] + cur_y
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or board[nx][ny] != 0: continue
                    board[nx][ny] = -1
                    queue.append((nx, ny))
                    cnt += 1
            res.append(cnt)
res.sort()
print(area)
for i in res:
    print(i, end=' ')