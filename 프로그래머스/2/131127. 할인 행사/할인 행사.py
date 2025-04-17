def solution(want, number, discount):
    answer = 0
    answer = sale(want, number, discount)
    return answer

def sale(want, number, discount):
    num = sum(number)
    ddict ={}
    start = 0
    end = num-1
    st = True
    cnt = 0
    for i in range(num):
        if discount[i] in ddict:
            ddict[discount[i]] += 1
        else:
            ddict[discount[i]] = 1
            
    while end < len(discount):
        for w, i in enumerate(want):
            if i not in ddict or ddict[i] == 0 or ddict[i] != number[w]:
                st = False
                continue

        if st:
            cnt += 1
            
        ddict[discount[start]] -= 1
        start += 1
        end += 1
        if end == len(discount):
            continue 
        if discount[end] in ddict:
            ddict[discount[end]] += 1
        else:
            ddict[discount[end]] = 1
        st = True
    return cnt