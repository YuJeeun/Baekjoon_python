import sys
inp = sys.stdin.readline

n, game = inp().split()
player = {inp().strip() for _ in range(int(n))}

if game == 'Y':
    j = 1
elif game == 'F':
    j = 2
else:
    j = 3

cnt = 0

for i in range(0, len(player)+1, j):
    cnt += 1

print(cnt-1)
