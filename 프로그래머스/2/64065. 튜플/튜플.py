from collections import defaultdict
def solution(s):
    answer = result(s)
    return answer





def result(str):
    ddict = defaultdict(int)
    llist = ''
    for s in str:
        if s == '{' or s == '}' or s == ',':
            if not llist:
                continue
            else:
                ddict[int(llist)] += 1
                llist = ''
        else:
            llist += s
    
    result = [0]*len(ddict)
    for key, value in ddict.items():
        result[len(ddict)-value] = key

    return result