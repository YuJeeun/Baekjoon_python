'''
n개의 자연수는 모두 다른 수
n개의 자연수 중 m개를 고른 수열

중복되는 수열 여러 번 출력 X
3 1
4 5 2
2 4
2 5
4 2
4 5
5 2
5 4 -> 일반 순열
'''

import sys
inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = list(map(int, inp().split()))
arr.sort()

visit = [0]*(max(arr)+1)

result = []

def dfs():
    if len(result) == m:
        for i in result:
            print(i, end=' ')
        print()
        return
    
    for i in arr:
        if visit[i] == 1: continue
        visit[i] = 1
        result.append(i)
        dfs()
        visit[i] = 0
        result.pop()
dfs()
        
    
