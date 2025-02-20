'''
키, 몸무게가 상대보다 더 크고 무거워야 덩치가 크다고 할 수 있음
'''

import sys
inp = sys.stdin.readline

n = int(inp())
people = [list(map(int, inp().split())) for _ in range(n)]
res = []
for i in range(1, n+1):
    cnt = 1
    for j in range(0, n):
        if people[i-1][0] < people[j][0] and people[i-1][1] < people[j][1]:
            cnt += 1
    res.append(cnt)

for i in res:
    print(i, end=' ')