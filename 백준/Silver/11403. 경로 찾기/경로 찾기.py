import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp())

graph = [list(map(int, inp().split())) for _ in range(n)]

result = []

queue = deque()

for i in range(n):
    visit = [0]*n
    queue.append(i)
    while queue:
        cur = queue.popleft() # i
        for j in range(n):
            if graph[cur][j] == 1 and not visit[j]:
                visit[j] = 1
                queue.append(j)
    result.append(visit)

for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()