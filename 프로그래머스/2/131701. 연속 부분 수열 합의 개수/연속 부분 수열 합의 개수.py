def solution(elements):
    res = set()
    cnt = 0

    while True:
        cnt += 1
        left, right = 0, cnt
        total = sum(elements[left: right])
        
        if cnt == len(elements):
            res.add(sum(elements))
            break
        
        res.add(total)
        
        for i in range(1, len(elements)):
            total -= elements[left]
            if right >= len(elements): total += elements[right-len(elements)]
            else: total += elements[right]
            res.add(total)    
            left, right = i, right + 1
    
    return len(res)
        