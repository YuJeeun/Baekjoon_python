T = int(input())

def minn(idx, result):
    global min_val
    if result >= min_val:
        return 
    
    if idx == n:
        if min_val > result:
            min_val = result
        return
    
    for i in range(n):
        if i in visited: continue
        visited.add(i)
        minn(idx+1, result+arr[idx][i])
        visited.remove(i)
        
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = set()
    result = 0
    min_val = int(1e9)
    minn(0, result)
    print(f'#{test_case}', min_val)
    