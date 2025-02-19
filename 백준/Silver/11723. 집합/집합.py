import sys
inp = sys.stdin.readline

m = int(inp())

s = set()
all = {i for i in range(1, 21)}

for _ in range(m):
    val = inp().split()
    if len(val) == 1:
        op = val[0]
    else:
        op, x = val[0], int(val[1])

    if op == 'add':
        s.add(x)
        continue
    if op == 'remove':
        if x in s:
            s.remove(x)
        continue
    if op == 'check':
        if x in s:
            print(1)
        else:
            print(0)
        continue
    if op == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
        continue
    if op == 'all':
        s=s.union(all)
        continue
    if op == 'empty':
        s.clear()
        continue
        

