import sys

inp = sys.stdin.readline

n = int(inp())

distance = list(map(int, inp().split()))
cost = list(map(int, inp().split()))

cur_cost = int(1e9)
res = 0

for i in range(n-1):    
    cur_cost = min(cur_cost, cost[i])
    res += cur_cost * distance[i]

print(res)