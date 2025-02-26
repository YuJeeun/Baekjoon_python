import sys
inp = sys.stdin.readline

n = int(inp())

res = []
def hanoi(n, start, end, by):
    if n == 1:
        res.append((start, end))
        return
    
    hanoi(n-1, start, by, end)
    res.append((start, end))
    hanoi(n-1, by, end, start)

hanoi(n,1,3,2)
print(len(res))
for i, j in res:
    print(i, j)