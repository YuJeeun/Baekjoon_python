import sys
inp = sys.stdin.readline
m,n = map(int, inp().split())
order = [inp().split() for _ in range(n)]
direction = {0:True, 1:False, 2:False, 3:False}
t = 0
x, y = 0, 0
for i in range(n):
    if (order[i][0].startswith("MOVE")):
        if (direction[0]):
            x+=int(order[i][1])
            if(x < 0 or x > m or y < 0 or y > m):
                print(-1)
                exit()
        elif (direction[1]):
            y+=int(order[i][1])
            if(x < 0 or x > m or y < 0 or y > m):
                print(-1)
                exit()
        elif (direction[2]):
            x-=int(order[i][1])
            if(x < 0 or x > m or y < 0 or y > m):
                print(-1)
                exit()
        elif (direction[3]):
            y-=int(order[i][1])
            if(x < 0 or x > m or y < 0 or y > m):
                print(-1)
                exit()
        
    else:
        if (order[i][1]=='0'):
            direction[t]=False
            t+=1
            if(t==4):
                t=0
                direction[t]=True
            else:
                direction[t]=True
        else:
            direction[t]=False
            t-=1
            if (t==-1):
                t=3
                direction[t]=True
            else: direction[t]=True
print(x, y)