import sys

inp = sys.stdin.readline

n = int(inp())

cnt = 0

for _ in range(n):
    ab = inp().strip()
    stack = []

    for i in ab:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if not stack:
        cnt += 1

print(cnt)
