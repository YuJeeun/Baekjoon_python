from collections import deque
def bfs(x, y, n):
    queue = deque()
    queue.append((x, 0))
    visited = set()
    visited.add(x)
    while queue:
        cur, cnt = queue.popleft()
        if cur == y:
            return cnt
        
        op = [cur+n, cur*2, cur*3]
        for i in range(len(op)):
            nx = op[i]
            if nx < 0 or nx > y or nx in visited: continue
            visited.add(nx)
            queue.append((nx, cnt+1))
            
    return -1

def solution(x, y, n):
    answer = 0
    answer = bfs(x, y, n)
    return answer