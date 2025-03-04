import sys
inp = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(inp())

def dfs(s):
    visited.add(s)
    selected_students.append(s)
    if graph[s] not in visited:
        dfs(graph[s])
    elif graph[s] in selected_students:
        team.update(selected_students[selected_students.index(graph[s]):])

for _ in range(t):
    n = int(inp())
    graph = [0] + list(map(int, inp().split()))

    visited = set() 
    team = set()

    for i in range(1, n+1):
        selected_students = list()
        dfs(i)
    print(n-len(team))