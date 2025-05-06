def solution(topping):
    cnt = 0
    ddict = {}
    topping_type = set(topping)

    for i in range(len(topping)):
        if topping[i] in ddict:
            ddict[topping[i]] += 1
        else:
            ddict[topping[i]] = 1
    type_cnt = len(ddict)
    piece = set()
    
    for i in range(len(topping)):
        ddict[topping[i]] -= 1
        
        if ddict[topping[i]] == 0:
            type_cnt -= 1
            
        piece.add(topping[i])
        
        if type_cnt == len(piece):
            cnt += 1
    
    return cnt

'''
1:2 2:1 3:1 4:1
토핑 총 4개 -> 각자 2개씩 가져가야 cnt +1
1가져가면
1:1 2:1 3:1 4:1

'''
# def solution(topping):
#     cnt = 0
#     for i in range(1, len(topping)):
#         piece1 = set(topping[:i])
#         piece2 = set(topping[i:])
#         if len(piece1) == len(piece2):
#             cnt += 1
#     return cnt