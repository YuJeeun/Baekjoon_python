import sys
import heapq

inp = sys.stdin.readline

n = int(inp())
m = int(inp())

graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v, w = map(int, inp().split())
    graph[u].append((v, w))

start,end = map(int, inp().split())

INF = int(1e9)
distance = [INF] * (n+1)
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

dijkstra(start)

print(distance[end])