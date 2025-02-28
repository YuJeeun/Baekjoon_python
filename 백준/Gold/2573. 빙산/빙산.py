# import sys
# from collections import deque
# inp = sys.stdin.readline

# n, m = map(int, inp().split())
# arr = [list(map(int, inp().split())) for _ in range(n)]
# melt = [[0]*m for _ in range(n)]
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# time = 0
# while True:
#     queue1 = deque()
#     queue2 = deque()
#     visit = [[0]*m for _ in range(n)]
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] != 0 and visit[i][j] == 0:
#                 queue2.append((i, j))
#                 visit[i][j] = 1
#                 while queue2:
#                     cur_x2, cur_y2 = queue2.popleft()
#                     for k in range(4):
#                         nx = dx[k] + cur_x2
#                         ny = dy[k] + cur_y2
#                         if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 0 or visit[nx][ny] == 1: continue
#                         queue2.append((nx, ny))
#                         visit[nx][ny] = 1
#                 cnt += 1

#     if cnt >= 2:
#         print(time)
#         exit()

#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 0:
#                 queue1.append((i, j))
    
#     while queue1:
#         cur_x1, cur_y1 = queue1.popleft()
#         for k in range(4):
#             nx = dx[k] + cur_x1
#             ny = dy[k] + cur_y1
#             if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 0: continue
#             melt[nx][ny] += 1
#     zero = 0
#     for i in range(n):
#         zero += arr[i].count(0)
#         if zero == n*m:
#             print(0)
#             exit()
#         for j in range(m):
#             arr[i][j] -= melt[i][j]
#             if arr[i][j] < 0:
#                 arr[i][j] = 0
            
#     time += 1

import sys
from collections import deque
inp = sys.stdin.readline

n, m = map(int, inp().split())
arr = [list(map(int, inp().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

time = 0
while True:
    queue = deque()
    visited = [[0]*m for _ in range(n)]
    melted = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and visited[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = 1
                while queue:
                    cur_x, cur_y = queue.popleft()
                    for k in range(4):
                        nx = dx[k] + cur_x
                        ny = dy[k] + cur_y
                        if nx >= 0 and ny >= 0 and nx < n and ny < m:
                            if arr[nx][ny] == 0:
                                melted[cur_x][cur_y] += 1
                            elif arr[nx][ny] != 0 and visited[nx][ny] == 0:
                                queue.append((nx, ny))
                                visited[nx][ny] = 1
                cnt += 1
                
    if cnt >= 2:
        print(time)
        exit()
    
    zero = 0
    for i in range(n):
        zero += arr[i].count(0)
        if zero == n*m:
            print(0)
            exit()
        for j in range(m):
            arr[i][j] -= melted[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0
    time += 1