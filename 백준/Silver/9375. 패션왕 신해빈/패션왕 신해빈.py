import sys

inp = sys.stdin.readline

case = int(inp())
count = 0
res_list = []
while count < case:
    res = 1
    count+=1
    clothes={}
    n = int(inp())
    clothes_list = [inp().split() for _ in range(n)]
    
    for c in clothes_list:
        clothes[c[0]] = c[1]
        
    for category in set(clothes.values()):
        res *= (list(clothes.values()).count(category)+1)

    res-=1
    res_list.append(res)

for r in res_list:
    print(r)
