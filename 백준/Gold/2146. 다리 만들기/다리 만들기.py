import sys
from collections import deque
inp = sys.stdin.readline

n = int(inp())
arr = [list(map(int, inp().split())) for _ in range(n)]

queue = deque() 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit = [[False]*n for _ in range(n)]
islands = dict()
islands_edge = dict()

def find_island():
    cnt = 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and not visit[i][j]:
                edge_coor = set()
                coor = set()
                queue.append((i, j))
                coor.add((i, j))
                visit[i][j] = True
                while queue:
                    cur_x, cur_y = queue.popleft()
                    for k in range(4):
                        nx = dx[k] + cur_x
                        ny = dy[k] + cur_y
                        if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny]: continue
                        if arr[nx][ny] == 0:
                            if (cur_x, cur_y) not in edge_coor:
                                edge_coor.add((cur_x, cur_y))
                            coor.add((cur_x, cur_y))
                        if arr[nx][ny] == 1:
                            queue.append((nx, ny))
                            coor.add((nx, ny))
                            visit[nx][ny] = True
                islands_edge[cnt] = edge_coor
                islands[cnt] = coor
                cnt += 1

find_island() 

min_bridge_length = int(1e9)

for i in range(1, len(islands_edge)+1):
    for x, y in islands_edge[i]:
            visit = [[False]*n for _ in range(n)]
            queue.append((x, y, 0))
            visit[x][y] = True
            while queue:
                cur_x, cur_y, cnt = queue.popleft()
                for k in range(4):
                    nx = dx[k] + cur_x
                    ny = dy[k] + cur_y
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny] or (nx, ny) in islands[i]: continue
                    if arr[nx][ny] == 0:
                        if min_bridge_length < cnt+1: continue
                        queue.append((nx, ny, cnt+1))
                        visit[nx][ny] = True
                    if arr[nx][ny] == 1:
                        min_bridge_length = min(min_bridge_length, cnt)       
print(min_bridge_length)