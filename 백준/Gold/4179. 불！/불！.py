import sys
from collections import deque

inp = sys.stdin.readline

r, c = map(int, inp().split())

arr = [inp().strip() for _ in range(r)]
maze = [[0]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        maze[i][j] = arr[i][j]

queue = deque()
cur = [0]*3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

F = []
J = []
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            F.append((i, j))
        elif maze[i][j] == 'J':
            J.append((i, j))

for i in range(len(F)):
    queue.append((F[i][0], F[i][1], 0))

queue.append((J[0][0], J[0][1], 0))

while queue:
    cur = queue.popleft()
    for i in range(4):
        nx = dx[i] + cur[0]
        ny = dy[i] + cur[1]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            if maze[cur[0]][cur[1]] == 'J':
                print(cur[2]+1)
                exit()
            else:
                continue
        if maze[nx][ny] != '.':    
            continue
        if maze[cur[0]][cur[1]] == 'F':
            maze[nx][ny] = 'F'
            queue.append((nx, ny, cur[2]+1))
        
        if maze[cur[0]][cur[1]] == 'J':
            maze[nx][ny] = 'J'
            queue.append((nx, ny, cur[2]+1))
print("IMPOSSIBLE")