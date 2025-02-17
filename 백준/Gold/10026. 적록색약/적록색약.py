import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp())
arr1 = [[0]*n for _ in range(n)]
arr2 = [inp().strip() for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr1[i][j] = arr2[i][j]

queue = deque()
cur = [0]*2

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    cnt = 0
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                queue.append((i, j))
                visit[i][j] = 1
                while queue:
                    cur = queue.popleft()
                    for k in range(4):
                        nx = dx[k] + cur[0]
                        ny = dy[k] + cur[1]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n or arr1[nx][ny] != arr1[cur[0]][cur[1]] or visit[nx][ny] == 1: continue
                        queue.append((nx, ny))
                        visit[nx][ny] = 1
                cnt += 1
    return cnt

print(bfs(), end=' ')

for i in range(n):
    for j in range(n):
        if arr1[i][j] == 'R':
            arr1[i][j] = 'G'

print(bfs())