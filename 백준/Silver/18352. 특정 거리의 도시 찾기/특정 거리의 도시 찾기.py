import sys
import heapq

inp = sys.stdin.readline

n, m, k, x = map(int, inp().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, inp().split())
    graph[a].append((b,1))

INF = int(1e9)
distance = [INF]*(n+1)

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (distance[start], start))

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(x)
cnt = 0
for i in range(len(distance)):
    if distance[i] == k:
        cnt += 1
        print(i)
if cnt == 0:
    print(-1)
    