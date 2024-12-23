'''
5 4 #달걀 개수, 잠재 고객
2   #P1
8   #P2
10  #P3
7   #P4
최대 수익을 낼 수 있는 가격을 찾는 방법?

1. 한 고객에게 두 개 이상의 달걀을 팔지 않음
2. 달걀 총 수량을 초과하여 판매할 수 없음

n>=m -> 기존대로
달걀의 개수가 고객 수 보다 적다면 -> ............ 
'''
# 1. 오름차순으로 정렬
# 2-1. 첫번째 가격으로 했을 경우 -> list[0]*m
# 2-2. 두번째 가격으로 했을 경우 -> list[1]*(m-1)
# 2-3. 세번째 가격으로 했을 경우 -> list[2]*(m-2)
# 2-4. 마지막 가격으로 했을 경우 -> list[m-1]*(m-3)
import sys
inp = sys.stdin.readline

n, m = list(map(int,inp().split()))
arr = []
p = {}
for i in range(m):
    arr.append(int(inp().strip()))
arr = sorted(arr)

for i in range(m):
    # # 1. 계란이 m-i개보다 많거나 같을때
    # if(n >= m-i):
    #     p[arr[i]] = arr[i]*(m-i)
    # # 2. 계란(n)이 m-i개 보다 적을때
    # else:
    #     p[arr[i]] = arr[i] * n

    p[arr[i]] = arr[i] * min(n, m-i)

for k, v in p.items():
    if(v==max(p.values())):
        print(k,v)
