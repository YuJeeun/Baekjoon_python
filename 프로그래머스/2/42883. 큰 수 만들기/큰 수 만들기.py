def solution(number, k):
    arr = []
    for num in number:
        while arr and k > 0 and arr[-1] < num:
            arr.pop()
            k -= 1
        arr.append(num)
    
    if k > 0:
        arr = arr[:len(arr)-k]
                
    return ''.join(arr)