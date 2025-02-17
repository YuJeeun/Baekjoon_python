import sys
from collections import deque

inp = sys.stdin.readline

'''
m: 가로, n: 세로
1: 익은 토마토, 0: 안익은 토마토, -1: 빈 칸
* 토마토는 하나 이상 존재
토마토가 모두 익을 때까지의 최소 날짜
이미 모두 익어있다면 0, 모두 익을 수 없는 상황이라면 -1
'''

m, n = map(int, inp().split())

box = [list(map(int, inp().split())) for _ in range(n)]

queue = deque()
cur = [0]*3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

zero = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            zero += 1
        if box[i][j] == 1:
            queue.append((i, j, 0))
            box[i][j] = -2

if zero == 0:
    print(0)
    exit()

while queue:
    cur = queue.popleft()
    for k in range(4):
        nx = dx[k] + cur[0]
        ny = dy[k] + cur[1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or box[nx][ny] != 0: continue
        box[nx][ny] = -2
        queue.append((nx, ny, cur[2]+1))

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()
            
print(cur[2])
