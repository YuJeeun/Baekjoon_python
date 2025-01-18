import sys
from collections import deque

inp = sys.stdin.readline

n, m = map(int, inp().split())

graph = [[] for _ in range(n+1)]

for i in range (m):
    u, v = map(int, inp().split())
    graph[u].append(v)
    graph[v].append(u)

queue = deque()
component = 0
cur = []
visit = [0] * (n+1)
for i in range (1,n+1):
    queue.append(i)
    if visit[i] == 0:
        visit[i] = 1
        while queue:
            cur = queue.popleft()
            for j in graph[cur]:
                if visit[j] == 0:
                    visit[j] = 1
                    queue.append(j)
        component+=1
print(component)