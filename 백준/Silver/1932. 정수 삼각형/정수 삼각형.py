import sys

inp = sys.stdin.readline

n = int(inp())

arr = [[0]*(n+1) for _ in range(0, n+1)]
num = [list(map(int, inp().split())) for _ in range(1, n+1)]

for i in range(1, n+1):
    for j in range(len(num[i-1])):
        arr[i][j+1] = num[i-1][j]

dp = [[0]*(n+1) for _ in range(0, n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[n]))