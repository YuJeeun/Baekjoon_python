import sys
inp = sys.stdin.readline

t = int(inp())

res = []
while t>0:
    ps = inp().strip().split()
    stack = []
    for i in range(len(ps[0])):
        if ps[0][i] == '(':
            stack.append(ps[0][i]) 
        elif ps[0][i] == ')':
            if not stack:
                stack.append(')')
                break
            else:
                stack.pop()
    if len(stack) == 0:
        res.append('YES')
    else:
        res.append('NO')
    t -= 1

for i in res:
    print(i)
