def solution(triangle):
    arr = [[0]*len(triangle[i]) for i in range(len(triangle))]
    arr[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0: arr[i][j] = arr[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1: arr[i][j] = arr[i-1][j-1] + triangle[i][j]
            else: arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + triangle[i][j]
    
    return max(arr[-1])
