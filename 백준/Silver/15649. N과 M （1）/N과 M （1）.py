import sys

inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = list()
for i in range(n):
    arr.append(i+1)

visit = [0]*n

result = []

def dfs():
    # result크기가 m이면 print
    if len(result) == m:
        for i in result:
            print(i, end=' ')
        print()
        return
    
    for i in range(n):
        if visit[i] == 1: continue
        visit[i] = 1
        result.append(arr[i])
        dfs()
        visit[i] = 0
        result.pop()

dfs()