import sys
from collections import deque

inp = sys.stdin.readline

n, m, k = map(int, inp().split())

xy = [list(map(int, inp().split())) for _ in range(k)]

arr = [[0]*(m+1) for _ in range(n+1)]
for i in range(k):
    arr[xy[i][0]][xy[i][1]] = 1

queue = deque()
cur = [0]*2

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i][j] == 1:
            cnt = 1
            queue.append([i, j])
            arr[i][j] = -1
            while queue:
                cur = queue.popleft()
                for k in range(4):
                    nx = dx[k] + cur[0]
                    ny = dy[k] + cur[1]
                    if nx < 0 or ny < 0 or nx >= n+1 or ny >= m+1 or not (arr[nx][ny] == 1): continue
                    queue.append([nx, ny])
                    arr[nx][ny] = -1
                    cnt += 1
            result.append(cnt)
print(max(result))
