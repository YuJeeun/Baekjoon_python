# 중복값이 있는 일반 조합
import sys
inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = list(map(int, inp().split()))
arr.sort()

result = []

def dfs(idx):
    if len(result) == m:
        for i in result:
            print(i, end=' ')
        print()
        return
    
    tmp = 0

    for i in range(idx, n):
        if tmp == arr[i]: continue
        result.append(arr[i])
        tmp = arr[i]
        dfs(i+1)
        result.pop()

dfs(0)
