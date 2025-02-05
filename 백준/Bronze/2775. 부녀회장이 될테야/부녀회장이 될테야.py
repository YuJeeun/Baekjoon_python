import sys

inp = sys.stdin.readline

t = int(inp())
res = []
while t!=0:
    t-=1
    
    k = int(inp())
    n = int(inp())

    dp = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1, n+1):
        dp[0][i] = i
    
    for i in range(1, k+1):
        for j in range(1, n+1):
            for l in range(1, j+1):
                dp[i][j] += dp[i-1][l]
    
    res.append(dp[k][n])

for i in res:
    print(i)