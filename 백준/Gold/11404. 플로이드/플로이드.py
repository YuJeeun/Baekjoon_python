import sys
inp = sys.stdin.readline

# 도시의 개수
n = int(inp())

# 버스의 개수
m = int(inp())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    # 시작 도시, 도착 도시, 필요한 비용
    a, b, c = map(int, inp().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else: print(graph[i][j], end=' ')
    print()
