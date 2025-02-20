import sys
inp = sys.stdin.readline

n, k = map(int, inp().split())

nation = []

for i in range(n):
    idx, g, s, b = map(int, inp().split())
    nation.append((g*100+s*10+b, idx))
nation.sort()
nation.reverse()

for j in range(n):
    if nation[j][1] == k:
        medal = nation[j][0]
        break

for l in range(n):
    if nation[l][0] == medal:
        print(l+1)
        break

