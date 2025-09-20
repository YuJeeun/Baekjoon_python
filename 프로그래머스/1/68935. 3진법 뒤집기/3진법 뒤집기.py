def solution(n):
    arr = trit(n)
    return int(arr,3)

def trit(n):
    arr = ''
    while n > 0:
        arr += str(n%3)
        n = n//3
    return arr
