'''
그래프를 DFS, BFS로 탐색한 결과 출력하기
단, 방문할 수 있는 정점이 여러 개인 경우 -> 정점 번호가 작은 것 먼저 방문
더이상 방문할 수 있는 점이 없는 경우 -> 종료
정점의 개수(1 <= N <= 1,000)
간선의 개수(1 <= M <= 10,000)
탐색을 시작할 정점의 번호 V
'''

import sys
from collections import deque
inp = sys.stdin.readline

n, m, v = map(int, inp().split())
visit = [0] * (n+1)
llist = [[] for _ in range(n+1)]
res_dfs = list()
res_bfs = list()
for i in range(m):
    a, b = map(int, inp().split())
    llist[a].append(b)
    llist[b].append(a)

for i in range(n+1):
    llist[i].sort()

visit[v] = v
res_dfs.append(visit[v])

#DFS
def dfs(v_num):
    for i in range(0, len(llist[v_num])):
        if visit[llist[v_num][i]] == 0:
            res_dfs.append(llist[v_num][i])
            visit[llist[v_num][i]] = 1
            dfs(llist[v_num][i])
dfs(v)
for i in res_dfs:
    print(i, end=' ')

# BFS
visit = [0] * (n+1) 
queue = deque()
queue.append([v, 0])
arr = [0] * 2

visit[v] = v
res_bfs.append(visit[v])

while len(queue) != 0:
    arr = queue.popleft()
    for i in range(0, len(llist[arr[0]])):
        if visit[llist[arr[0]][i]] == 0:
            res_bfs.append(llist[arr[0]][i])
            visit[llist[arr[0]][i]] = 1
            queue.append([llist[arr[0]][i], arr[1]+1])
print()
for i in res_bfs:
    print(i, end= ' ')
