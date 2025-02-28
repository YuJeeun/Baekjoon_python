import sys
from collections import deque
inp = sys.stdin.readline

n, m = map(int, inp().split())
arr = [list(map(int, inp().split())) for _ in range(n)]
melted = dict()
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            melted[(i, j)] = arr[i][j]
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

time = 0
while True:
    queue = deque()
    visited = set()
    cnt = 0
    melted = {k:v for k,v in melted.items() if v > 0}
    for keys, values in melted.items():
        if keys in visited: continue
        queue.append(keys)
        visited.add(keys)
        while queue:
            cur_x, cur_y = queue.popleft()
            for k in range(4):
                nx = dx[k] + cur_x
                ny = dy[k] + cur_y
                if nx >= 0 and ny >= 0 and nx < n and ny < m:
                    if arr[nx][ny] == 0:
                        melted[(cur_x, cur_y)] -= 1
                    elif arr[nx][ny] != 0 and (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        cnt += 1

    if cnt >= 2:
        print(time)
        exit()

    if cnt == 0:
        print(0)
        exit()

    for keys in melted.keys():
        if melted[keys] < 0:
            melted[keys] = 0
        arr[keys[0]][keys[1]] = melted[keys]

    time += 1