import sys
inp = sys.stdin.readline

n = int(inp())
coin_prices = list(map(int, inp().split()))
maxx = max(coin_prices)
income = 0

for i in range(n):
    if coin_prices[i] < maxx:
        income += maxx-coin_prices[i]
    elif coin_prices[i] == maxx:
        if i+1 < n:
            maxx = max(coin_prices[i+1:])
print(income) 