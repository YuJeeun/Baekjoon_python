import sys
inp = sys.stdin.readline

n, k = map(int, inp().split())
strr = list(inp())
p_list = list()
cnt = 0
for i in range(n):
    if strr[i] == 'P':
        p_list.append(i)

for p in p_list:
    for i in range(p-k, p+k+1):
        if i < 0 or i >= n:
            continue
        if strr[i] == 'H':
            strr[i] = 'E'
            cnt += 1
            break
print(cnt)
