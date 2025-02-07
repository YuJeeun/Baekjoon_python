import sys

inp = sys.stdin.readline

n = int(inp())

arr = [0]*(n+1)
for i in range(1, n+1):
    arr[i] = int(inp().strip())

dp = [[0]*3 for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = arr[1]
dp[1][2] = arr[1]

for i in range(2, n+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = max(dp[i-2][0], dp[i-2][1], dp[i-2][2]) + arr[i]
    dp[i][2] = dp[i-1][1] + arr[i]

result = []
for i in range(n+1):
    result.append(dp[i][0])
    result.append(dp[i][1])
    result.append(dp[i][2])

print(max(result))