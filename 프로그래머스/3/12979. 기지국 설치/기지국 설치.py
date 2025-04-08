import math
def solution(n, stations, w):
    l = w*2+1 # 전파 범위
    cnt = 0
    for i in range(len(stations)):
        pre = 0 if i == 0 else stations[i-1]+w+1
        cur = stations[i]-w-1
        if cur+1 <= 1 or pre-1 >= cur: continue
        cnt += int((cur-pre)/l) + 1
        
    if stations[-1]+w < n:
        cnt += int((n-(stations[-1]+w+1))/l) + 1

    return cnt