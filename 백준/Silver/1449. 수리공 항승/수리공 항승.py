import sys
inp = sys.stdin.readline

n, l = map(int, inp().split())
x_list = list(map(int, inp().split()))

x_list.sort()
taped = set()
cnt = 0

for x in range(n):
    if x_list[x] not in taped:
        if x+1 == n:
            cnt += 1
            break
        for y in range(x+1, n):
            taped.add(x_list[x])
            if abs(x_list[x]-x_list[y]) < l:
                taped.add(x_list[y])
        cnt += 1
print(cnt)