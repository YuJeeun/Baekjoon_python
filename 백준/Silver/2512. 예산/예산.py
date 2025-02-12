import sys
inp = sys.stdin.readline

n = int(inp())

area = list(map(int, inp().split()))
area.sort()

m = int(inp())

start = 1
end = area[-1]
mid = 0
max_mid = 0
while start <= end:
    total_allotment = 0
    mid = (start+end)//2
    for i in range(n):
        if area[i] < mid:
            total_allotment += area[i]
        else:
            total_allotment += mid

    if total_allotment < m:
        start = mid + 1
        max_mid = max(max_mid, mid)    
    elif total_allotment > m:
        end = mid - 1
    else: 
        max_mid = max(max_mid, mid)
        break
print(max_mid)    