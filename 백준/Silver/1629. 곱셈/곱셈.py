import sys
inp = sys.stdin.readline

a, b, c = map(int, inp().split())

llist = []
while b>1:
    if b%2==0:
        b=b/2
        llist.append(0)
    else:
        b=b-1
        b=b/2
        llist.append(1)

res = a%c
for i in range(len(llist)-1, -1, -1):
    if llist[i] == 0:
        res = (res*res)%c
    else:
        res = (res*res)%c*a%c
print(res)