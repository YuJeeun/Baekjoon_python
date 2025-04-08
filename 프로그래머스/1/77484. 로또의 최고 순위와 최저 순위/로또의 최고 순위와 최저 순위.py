def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = 0
    ddict = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
        elif lotto == 0:
            zero += 1
    answer = [ddict[zero+cnt], ddict[cnt]]
    return answer