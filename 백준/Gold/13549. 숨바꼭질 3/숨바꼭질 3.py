import sys
from collections import deque
inp = sys.stdin.readline

n, k = map(int, inp().split())

queue = deque()
queue.append(n)

INF = int(1e9)
visit = [INF]*100001
visit[n] = 0

while queue:
    cur = queue.popleft()

    if cur == k:
        print(visit[cur])
        exit()

    nx = cur*2

    if 0 <= nx <= 100000 and visit[nx] > visit[cur]:
        visit[nx] = visit[cur]
        queue.appendleft(nx)
    
    nx = cur+1

    if 0 <= nx <= 100000 and visit[nx] > visit[cur]+1:
        visit[nx] = visit[cur]+1
        queue.append(nx)

    nx = cur-1

    if 0 <= nx <= 100000 and visit[nx] > visit[cur]+1:
        visit[nx] = visit[cur]+1
        queue.append(nx)
    