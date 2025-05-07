def dp(land, arr):
    for i in range(1, len(land)):
        arr[i][0] = land[i][0] + max(arr[i-1][1], arr[i-1][2], arr[i-1][3])
        arr[i][1] = land[i][1] + max(arr[i-1][0], arr[i-1][2], arr[i-1][3])
        arr[i][2] = land[i][2] + max(arr[i-1][1], arr[i-1][0], arr[i-1][3])
        arr[i][3] = land[i][3] + max(arr[i-1][1], arr[i-1][2], arr[i-1][0])
        
def solution(land):
    answer = 0
    arr = [[0]*4 for _ in range(len(land))]
    
    for i in range(4):
        arr[0][i] = land[0][i]
        
    dp(land, arr)
    
    answer = max(arr[-1])
    return answer
