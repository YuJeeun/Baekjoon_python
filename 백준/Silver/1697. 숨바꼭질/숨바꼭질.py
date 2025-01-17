import sys
from collections import deque

inp = sys.stdin.readline

n, k = map(int, inp().split())

queue = deque()
queue.append([n, 0])
cur = [0]*2

matrix = [0] * 100001
matrix[n] = 1
if k == n: 
    print(0)
    exit()
while queue:
    cur = queue.popleft()
    dx = cur[0]+1, cur[0]-1, cur[0]*2
    for i in range(3):
        nx = dx[i]
        if nx < 0 or nx > 100000: continue
        if matrix[nx] == 0:
            matrix[nx] = 1
            queue.append([nx, cur[1]+1])
        if nx == k:
            print(cur[1]+1)
            exit()
            
        
