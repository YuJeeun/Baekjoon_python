import sys
inp = sys.stdin.readline

n = int(inp())
n_list = list(map(int, inp().split()))

m = int(inp())
m_list = list(map(int, inp().split()))

n_list.sort()

for i in range(m):
    start = 0
    end = n-1
    mid = 0

    while start <= end:
        mid = (start + end) // 2
        if m_list[i] == n_list[mid]:
            print(1)
            break
        if m_list[i] < n_list[mid]:
            end = mid - 1
        else:
            start = mid + 1

    if m_list[i] != n_list[mid]:
        print(0)
    