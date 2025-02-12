import sys
import heapq
inp = sys.stdin.readline

n, m, x = map(int, inp().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, t = map(int, inp().split())
    graph[a].append((b, t))

INF = int(1e9)
distance = [INF]*(n+1)

res = []
test = []
def dijkstra():
    for i in range(1, n+1):
        distance = [INF]*(n+1)

        queue = []
        distance[i] = 0
        heapq.heappush(queue, (distance[i], i))
        while queue:
            dist, now = heapq.heappop(queue)
            if distance[now] < dist: continue
            for k in graph[now]:
                cost = dist + k[1]
                if cost < distance[k[0]]:
                    distance[k[0]] = cost
                    heapq.heappush(queue, (cost, k[0]))
        res.append(distance)
    
dijkstra()
for i in range(len(res)):
    test.append(res[i][x]+res[x-1][i+1])
print(max(test))
