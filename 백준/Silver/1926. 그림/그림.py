import sys
from collections import deque

inp = sys.stdin.readline

n, m = map(int, inp().split())

board = [list(map(int, inp().split())) for _ in range(n)]

queue = deque()

cur = [0]*2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 그림 개수, 가장 넓은 그림 넓이
area = []
cnt = 0


for i in range(n):
    for j in range(m):
        c = 1
        if board[i][j] == 1:
            queue.append((i, j))
            board[i][j] = -1
            while queue:
                cur = queue.popleft()
                for k in range(4):
                    nx = dx[k] + cur[0]
                    ny = dy[k] + cur[1]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] != 1: continue
                    queue.append((nx, ny))
                    board[nx][ny] = -1
                    c += 1
            area.append(c)        
            cnt += 1
if cnt == 0:
    print(0)
    print(0)
    exit()

print(cnt)
print(max(area))