import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp()) # 컴퓨터의 수
e = int(inp()) # 연결되어 있는 컴퓨터 쌍의 수

llist = [[] for _ in range(n+1)]

for i in range(e):
    a, b = map(int, inp().split())
    llist[a].append(b)
    llist[b].append(a)

visit = [0]*(n+1)

queue = deque()
queue.append([1, 0])
visit[1] = 1
while queue:
    cur = queue.popleft()
    for i in range(len(llist[cur[0]])):
        if visit[llist[cur[0]][i]] == 0:
            visit[llist[cur[0]][i]] = 1
            queue.append([llist[cur[0]][i], cur[1]+1])

print(visit.count(1)-1)
