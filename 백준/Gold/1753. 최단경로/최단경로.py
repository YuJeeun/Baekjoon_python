import sys
import heapq

inp = sys.stdin.readline

v_num, e = map(int, inp().split())
start = int(inp())

graph = [[] for _ in range(v_num+1)]

for i in range(e):
    u, v, w = map(int, inp().split())
    graph[u].append((v, w)) # u->v 가중치 w

INF = int(1e9)
distance = [INF] * (v_num+1)

def dijkstra(start):
    queue = []
    distance[start] = 0 
    heapq.heappush(queue, (distance[start], start)) # 거리, 시작정점
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist: continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)
for i in range(1, len(distance)):
    if distance[i]==INF:
        print('INF')
    else: print(distance[i])
            

