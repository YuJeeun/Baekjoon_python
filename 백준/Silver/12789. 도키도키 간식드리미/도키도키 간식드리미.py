from collections import deque
import sys
inp = sys.stdin.readline
'''
5           #승환이 앞에 서 있는 학생들의 수 N
5 4 1 3 2   #승환이 앞에 서 있는 모든 학생들의 번호표
'''
n = int(inp())
line = deque(map(int,inp().split()))
stck = deque()
s = deque()
start = 1
while line:
    cur = line.popleft()
    if (cur == start):
        s.append(cur)
        start+=1
    else:
        while stck and stck[-1] == start:
            stck.pop()
            start+=1
        stck.append(cur)

while stck:
    if stck[-1] == start:
        stck.pop()
        start += 1
    else:
        print("Sad")
        exit()

print("Nice")
