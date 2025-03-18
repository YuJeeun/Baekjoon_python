import sys
inp = sys.stdin.readline

n, x = map(int, inp().split())
visited = [0] + list(map(int, inp().split()))
dp = [0]*(n+1)
dp[1] = visited[1]
for i in range(2, n+1):
    if i-x >= 0:
        dp[i] = visited[i] + dp[i-1] - visited[i-x]
    else:
        dp[i] = visited[i] + dp[i-1]
maxx = max(dp)
print('SAD') if maxx == 0 else print(maxx, dp.count(maxx), sep='\n')