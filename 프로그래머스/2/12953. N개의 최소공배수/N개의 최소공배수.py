def solution(arr):
    answer = 1
    answer = gcd(arr)
    return answer

def gcd(arr):
    for i in range(len(arr)-1):
        a = max(arr[i], arr[i+1])
        b = min(arr[i], arr[i+1])
        while b>0:
            a, b = b, a%b
        arr[i+1] = arr[i]*arr[i+1]//a
    return arr[-1]