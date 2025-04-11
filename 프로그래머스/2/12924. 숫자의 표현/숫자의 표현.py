def solution(n):
    n_list = [0]+[i for i in range(1, n+1)]
    start, end = 1, 1
    cnt = 0
    while True:
        if start == end:
            if start == n:
                cnt += 1
                return cnt
            else:
                end += 1
                continue
        
        if sum(n_list[start:end+1]) == n:
            cnt += 1
            start += 1
            continue
        
        elif sum(n_list[start:end+1]) < n:
            end += 1
            continue
            
        else:
            start += 1
            continue