'''
0 0 3 5 2 4 9 0 6 4 0 6 0 0
n일때 n-2 ~ n+2 중 하나라도 n이상인 수가 있으면 continue
아니면 n-범위내가장큰수 result에 더하기

'''

T = 10

for test_case in range(1, T+1):
    n = int(input())
    bulidings = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2): # 2, 8
        if bulidings[i-2] >= bulidings[i] or bulidings[i-1] >= bulidings[i] or bulidings[i+1] >= bulidings[i] or bulidings[i+2] >= bulidings[i]:
            continue
        maxx = max(bulidings[i-2], bulidings[i-1], bulidings[i+1], bulidings[i+2])
        result += bulidings[i] - maxx
        
    print(f'#{test_case}', result)
        
    