T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [[1]*i for i in range(1,n+1)]
    idx1, idx2 = 3, 2
    for i in range(2, n):
        for j in range(len(arr[i])):
            if j == 0 or j == len(arr[i])-1:
                continue
            arr[i][j] = arr[i-1][j-idx1] + arr[i-1][j-idx2]
        idx1 += 1
        idx2 += 1
    print(f'#{test_case}')
    for i in range(len(arr)):
        print(*arr[i])