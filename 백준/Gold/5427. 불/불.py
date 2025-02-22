'''
'.': 빈 공간
'#': 벽
'@': 상근이~
'*': 불
'''
import sys
from collections import deque

inp = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = int(inp())
for _ in range(t):
    w, h = map(int, inp().split())
    building = [list(inp().strip()) for _ in range(h)]
    
    queue = deque()
    F = []
    S = []
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                F.append((i, j))
            elif building[i][j] == '@':
                S.append((i, j))

    for i in range(len(F)):
        queue.append((F[i][0], F[i][1], 0))
    queue.append((S[0][0], S[0][1], 0))
    res = 0
    while queue:
        cur_x, cur_y, time = queue.popleft()
        for j in range(4):
            nx = dx[j] + cur_x
            ny = dy[j] + cur_y
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                if building[cur_x][cur_y] == '@':
                    queue.clear()
                    res = time+1
                    break
                else:
                    continue

            if building[nx][ny] != '.': continue
            
            if building[cur_x][cur_y] == '*':
                building[nx][ny] = '*'
                queue.append((nx, ny, time + 1))
            
            if building[cur_x][cur_y] == '@':
                building[nx][ny] = '@'
                queue.append((nx, ny, time + 1))
            
    print('IMPOSSIBLE'if res == 0 else res)