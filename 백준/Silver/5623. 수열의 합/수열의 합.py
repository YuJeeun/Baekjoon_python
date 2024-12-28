import sys
inp = sys.stdin.readline

n = int(inp())
s = [list(map(int, inp().split())) for _ in range(n)]
arr = [0]*n

if (n==2):
    print(1, 1)
    exit()
else: 
    arr[0]=int((s[0][2]+s[1][0]-s[2][1])/2)
    print(arr[0], end=' ')
    for i in range(1, n):
        arr[i]=s[i][i-1]-arr[i-1]
        print(arr[i], end=' ')
    




