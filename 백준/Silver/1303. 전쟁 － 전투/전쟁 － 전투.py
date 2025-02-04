import sys
from collections import deque

inp = sys.stdin.readline

n, m = map(int, inp().split())

arr1 = [[0]*n for _ in range(m)]
arr2 = [inp().strip() for _ in range(m)] 

for i in range(m):
    for j in range(n):
        arr1[i][j] = arr2[i][j]
        
queue = deque()
visit = [[0]*n for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cur = [0]*2

result = {'W': 0, 'B': 0}

for i in range(m):
    for j in range(n):
        if visit[i][j] == 0:
            cnt = 1
            queue.append([i, j])
            visit[i][j] = 1
            color = arr1[i][j]
            while queue:
                cur = queue.popleft()
                for k in range(4):
                    nx = dx[k] + cur[0]
                    ny = dy[k] + cur[1]
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or not (arr1[nx][ny] == arr1[cur[0]][cur[1]]) or visit[nx][ny] == 1: continue
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
                    cnt+=1
            if color == 'W':
                result['W'] += pow(cnt,2)
            else: result['B'] += pow(cnt,2)

print(result['W'], result['B'])
