import sys

inp = sys.stdin.readline

n = int(inp())

dp = [0]*(n+1)
if n==1:
    print(0)
    exit()
elif n==2:
    print(1)
    exit()

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    if i%6==0:
        dp[i] = min(dp[int(i/3)]+1, dp[int(i/2)]+1, dp[i-1]+1)
    elif i%3==0:
        dp[i] = min(dp[int(i/3)]+1, dp[i-1]+1)
    elif i%2==0:
        dp[i] = min(dp[int(i/2)]+1, dp[i-1]+1)
    else:
        dp[i] = dp[i-1]+1

print(dp[n])