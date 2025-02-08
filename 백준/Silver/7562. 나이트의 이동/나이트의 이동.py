import sys
from collections import deque

inp = sys.stdin.readline

t = int(inp())

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

res = []

def bfs(l, start_x, start_y, end_x, end_y):
    cur = [0]*3
    queue = deque()
    queue.append([start_x, start_y, 0])
    visit[start_x][start_y] = 1
    while queue:
        cur = queue.popleft()

        if cur[0] == end_x and cur[1] == end_y:
            res.append(cur[2])
            return
        
        for i in range(8):
            nx = dx[i] + cur[0]
            ny = dy[i] + cur[1]
            if nx < 0 or ny < 0 or nx >= l or ny >= l or visit[nx][ny] == 1: continue
            if nx == end_x and ny == end_y:
                visit[nx][ny] = 1
                res.append(cur[2]+1)
                return
            
            visit[nx][ny] = 1
            queue.append([nx, ny, cur[2]+1])

for _ in range(t):
    l = int(inp())

    board = [[0]*l for _ in range(l)]

    visit = [[0]*l for _ in range(l)]

    start_x, start_y = map(int, inp().split())
    end_x, end_y = map(int, inp().split())

    bfs(l, start_x, start_y, end_x, end_y)

for i in res:
    print(i)

