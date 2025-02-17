import sys
from collections import deque

inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = [inp().strip() for _ in range(n)]
maze = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        maze[i][j] = int(arr[i][j])

queue = deque()
queue.append((0, 0, 1))
maze[0][0] = -1
cur = [0]*3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    cur = queue.popleft()
    for i in range(4):
        nx = dx[i] + cur[0]
        ny = dy[i] + cur[1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or maze[nx][ny] != 1: continue
        queue.append((nx, ny, cur[2]+1))
        maze[nx][ny] = -1

        if nx == n-1 and ny == m-1:
            print(cur[2]+1)
            exit()