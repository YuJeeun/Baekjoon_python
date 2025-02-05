import sys

inp = sys.stdin.readline

n = int(inp())

res = 0

while n>=0:
    if n%5 == 0:
        res += n/5
        print(int(res))
        exit()
    n = n-3
    res += 1

print(-1)
