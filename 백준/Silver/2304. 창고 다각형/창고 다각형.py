import sys
inp = sys.stdin.readline

n = int(inp())

tower = [list(map(int, inp().split())) for _ in range(n)]
tower.sort()

maxx_arr = max(tower, key=lambda x: x[1])
maxx_index = tower.index(maxx_arr)

area = maxx_arr[1]

height = tower[0][1]

for i in range(maxx_index):
    if height < tower[i+1][1]:
        area += height*(tower[i+1][0]-tower[i][0])
        height = tower[i+1][1]
    else:
        area += height*(tower[i+1][0]-tower[i][0])

height = tower[-1][1]

for i in range(n-1, maxx_index, -1):
    if height < tower[i-1][1]:
        area += height*(tower[i][0]-tower[i-1][0])
        height = tower[i-1][1]
    else:
        area += height*(tower[i][0]-tower[i-1][0])  

print(area)
