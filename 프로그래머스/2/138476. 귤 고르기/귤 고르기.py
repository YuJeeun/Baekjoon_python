from collections import Counter
def solution(k, tangerine):
    ddict = Counter(tangerine)
    llist = sorted(ddict.values(), reverse = True) 
    cnt = 0
    val = k
    for value in llist:
        if k <= value:
            return 1
        if val <= 0:
            return cnt
        else:
            val -= value
            cnt +=1
    return cnt