import sys

inp = sys.stdin.readline

n = int(inp())

arr = [[0, 0]]*(n+2)
for i in range(1, n+1):
    arr[i] = list(map(int, inp().split()))

dp = [0]*(n+2)

for i in range(1, n+2):
    dp[i] = max(dp[i], dp[i-1])
    if (i+arr[i][0]) > (n+1): continue
    dp[i+arr[i][0]] = max(dp[i]+arr[i][1], max(dp[arr[i][0]+i], dp[arr[i][0]+i-1]))

print(dp[n+1])