from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    
    for start, end in wires:
        graph[start].append(end)
        graph[end].append(start)
    
    mmin = int(1e9)
    
    for start, end in wires:
        graph[start].remove(end)
        graph[end].remove(start)
        
        mmin = min(abs(bfs(n, start, graph) - bfs(n, end, graph)), mmin)
        
        graph[start].append(end)
        graph[end].append(start)
    
    return mmin

def bfs(n, idx, graph):
    visited = [0]*(n+1)
    visited[idx] = 1
    queue = deque([idx])
    cnt = 1
    
    while queue:
        cur = queue.popleft()
        
        for i in graph[cur]:
            if visited[i] == 1: continue
            queue.append(i)
            visited[i] = 1
            cnt += 1
    
    return cnt
    