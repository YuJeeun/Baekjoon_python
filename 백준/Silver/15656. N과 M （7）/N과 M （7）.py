import sys

inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = list(map(int, inp().split()))
arr.sort()

result = []

def dfs():
    if len(result) == m :
        for i in result:
            print(i, end=' ')
        print()
        return
    
    for i in range(n):
        result.append(arr[i])
        dfs()
        result.pop()

dfs()