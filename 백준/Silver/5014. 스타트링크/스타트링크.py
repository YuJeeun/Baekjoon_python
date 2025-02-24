import sys
from collections import deque
inp = sys.stdin.readline

f, s, g, u, d = map(int, inp().split())

queue = deque()
queue.append((s, 0))
visit = [False] * (f+1)
visit[s] = True

while queue:
    cur_x, cnt = queue.popleft()
    if cur_x == g:
        print(cnt)
        exit()
    for i in [u, -d]:
        nx = cur_x + i
        if nx < 1 or nx > f or visit[nx]: continue
        visit[nx] = True
        queue.append((nx, cnt+1))

print('use the stairs')