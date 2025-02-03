import sys

inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = list(map(int, inp().split()))
arr.sort()

visit = [0]*n
result = []

def dfs():
    if len(result) == m:
        for i in result:
            print(i, end=' ')
        print()
        return
    
    tmp = 0 

    for i in range(n):
        if visit[i] == 1 or tmp == arr[i]: continue
        visit[i] = 1
        tmp = arr[i]
        result.append(arr[i])
        dfs()
        visit[i] = 0
        result.pop()

dfs()
