def solution(n):
    answer = 0
    answer = jump(n)
    return answer

def jump(n):
    arr = [[0] for _ in range(n+1)]
    arr[1] = 1
    if n == 1:
        return 1
    arr[2] = 2
    for i in range(3, len(arr)):
        arr[i] = arr[i-2] + arr[i-1]
    
    return arr[n]%1234567
    