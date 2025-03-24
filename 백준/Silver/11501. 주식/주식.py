import sys
inp = sys.stdin.readline

t = int(inp())

for _ in range(t):
    n = int(inp())
    stocks = list(map(int, inp().split()))

    maxx = stocks[-1]
    money = 0

    for i in range(n-2, -1, -1):
        if maxx > stocks[i]:
            money += maxx - stocks[i]
        else:
            maxx = stocks[i]
    print(money)