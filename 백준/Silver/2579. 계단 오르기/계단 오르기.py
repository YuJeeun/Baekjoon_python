import sys

inp = sys.stdin.readline

n = int(inp())

arr = [0]*(n+1)
for i in range(1, n+1):
    arr[i] = int(inp().strip())

dp = [[0]*2 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[i][0] = 0
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + arr[i]
    dp[i][1] = dp[i-1][0] + arr[i]

print(max(dp[n][0], dp[n][1]))