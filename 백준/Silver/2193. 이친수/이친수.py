import sys
inp = sys.stdin.readline

n = int(inp())

dp = [[0]*2 for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = 1
if n == 1:
    print(sum(dp[1]))
    exit()
dp[2][0] = 1
dp[2][1] = 0

for i in range(3, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

print(sum(dp[n]))