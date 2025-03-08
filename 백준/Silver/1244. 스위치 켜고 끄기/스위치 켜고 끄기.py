import sys
inp = sys.stdin.readline

n = int(inp())
switches = [0] + list(map(int, inp().split()))
t = int(inp())

for _ in range(t):
    s, num = map(int, inp().split())

    if s == 1:
        for i in range(num, n+1, num):
            switches[i] = abs(switches[i]-1)
    else:
        for i in range(1, int((n+1)/2)):
            if num-i > 0 and num+i <= n:
                if switches[num-i] == switches[num+i]:
                    switches[num-i] = abs(switches[num-i]-1)
                    switches[num+i] = abs(switches[num+i]-1)
                else:
                    break
        switches[num] = abs(switches[num]-1)
for j in range(1, len(switches)):
    print(switches[j], end=' ')
    if j%20==0: print()