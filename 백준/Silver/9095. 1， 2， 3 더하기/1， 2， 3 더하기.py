import sys

inp = sys.stdin.readline

t = int(inp())

dp = [0]*11

res = []
while t!=0:
    n = int(inp())
    t-=1

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    res.append(dp[n])

for i in res:
    print(i)

