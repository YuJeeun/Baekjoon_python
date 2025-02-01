'''
자연수 n, m
- 1부터 n까지 자연수 중 m개를 고른 수열
- 같은 수 여러 번 -> 중복 O
- 비내림차순

중복되는 수열을 여러 번 출력할 수 없음
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
-> 중복 조합
'''

import sys
inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = []
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
        dfs(i)
        result.pop()

dfs(0)

