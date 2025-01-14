import sys
from collections import deque
inp = sys.stdin.readline

n, m = map(int, inp().split())

matrix = [[0] * m for _ in range(n)]

for i in range(n):
    str = inp().strip()
    for j in range(len(str)):
        matrix[i][j] = int(str[j])

queue = deque()
queue.append([0, 0, 1])

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr = [0] * 3
matrix[0][0] = 2

while len(queue) !=0: # 큐가 빌때까지 반복
    arr = queue.popleft() # x, y, 거리
    if arr[0]==n-1 and arr[1]==m-1:
        print(arr[2])
        exit()
    for i in range(4):
        nx = arr[0] + dx[i]
        ny = arr[1] + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or matrix[nx][ny] == 0: continue
        if matrix[nx][ny] == 1:
            matrix[nx][ny] = arr[2] + 1
            queue.append([nx, ny, arr[2] + 1])
print(arr[2])