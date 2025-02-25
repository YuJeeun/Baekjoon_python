import sys
from collections import deque
inp = sys.stdin.readline


while True:
    l, r, c = map(int, inp().split())
    if l == 0 or r == 0 or c == 0:
        exit()
    building = [[[] for _ in range(r)] for _ in range(l)]
    llist = []
    for i in range(l):
        for j in range(r+1):
            arr = inp().strip()
            if not arr:
                continue
            llist.append(arr)

    idx = 0
    for i in range(l):
        for j in range(r):
            building[i][j] = list(llist[idx])
            idx += 1

    queue = deque()
    visit = [[[False]*c for _ in range(r)] for _ in range(l)]
    res = False
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S' and not visit[i][j][k]:
                    queue.append((i, j, k, 0))
                    visit[i][j][k] = True
                    while queue:
                        cur_z, cur_x, cur_y, time = queue.popleft()
                        if building[cur_z][cur_x][cur_y] == 'E':
                            print(f'Escaped in {time} minute(s).')
                            res = True
                        else:
                            for o in range(6):
                                nz = cur_z + dz[o]
                                nx = cur_x + dx[o]
                                ny = cur_y + dy[o]
                                if nz < 0 or nx < 0 or ny < 0 or nz >= l or nx >= r or ny >= c or visit[nz][nx][ny] or building[nz][nx][ny] == '#': continue
                                visit[nz][nx][ny] = True
                                queue.append((nz,nx,ny,time+1))
    if not res:
        print('Trapped!')