'''
피보나치 함수를 호출했을 때
0 과 1이 각각 몇 번 출력되는지
t
n
'''
import sys

inp = sys.stdin.readline

t = int(inp())
cnt = 0

d = dict()

d[0] = [1, 0]
d[1] = [0, 1]
d[2] = [1, 1]

result = []

while cnt < t:
    n = int(inp())
    
    for i in range(3, n+1):
        d[i] = [d[i-1][0]+d[i-2][0], d[i-1][1]+d[i-2][1]]

    result.append([d[n][0], d[n][1]])

    cnt += 1

for i in result:
    print(i[0], i[1])

