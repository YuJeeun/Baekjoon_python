# 일반 조합 1,2랑 2,1은 같은거임 순서가 없으니까

import sys

inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = list()
for i in range(n):
    arr.append(i+1)

result = []

def dfs(idx):
    if len(result) == m:
        for i in result:
            print(i, end=' ')
        print()
        return

    for i in range(idx, n):
        result.append(arr[i])
        dfs(i+1)
        result.pop()

dfs(0)