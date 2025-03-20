import sys
from collections import deque
inp = sys.stdin.readline

a, b = map(int, inp().split())

queue = deque()

queue.append((a, 1))

def bfs():
    while queue:
        cur, cnt = queue.popleft()
        if cur == b:
            print(cnt)
            exit()
        dx = [cur*2, cur*10+1]
        for i in range(2):
            nx = dx[i]
            if nx > b: continue
            queue.append((nx, cnt+1))
    print(-1)
bfs()