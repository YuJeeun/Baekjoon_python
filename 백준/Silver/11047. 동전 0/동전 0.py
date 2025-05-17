'''
1 <= n <= 10
1 <= k <= 100,000,000
오름차순
k원을 만드는데 필요한 동전 개수의 최솟값
'''

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0
for i in range(n-1, -1, -1):
    if k == 0: break
    if k < coins[i]: continue
    cnt += k//coins[i]
    k = k%coins[i]

print(cnt)
