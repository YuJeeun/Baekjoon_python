# def solution(msg):
#     answer = []
#     left = 0
#     right = 1
#     alist = [chr(i) for i in range(ord('A'),ord('Z')+1)]
#     ddict = {alist[i]: i+1 for i in range(26)}
#     last_val = ddict['Z']

#     while left < right:
#         if left == len(msg)-1:
#             answer.append(ddict[msg[-1]])
#             break
            
#         if msg[left:right] in ddict:
#             right += 1

#         else:
#             last_val += 1
#             ddict[msg[left:right]] = last_val
#             answer.append(ddict[msg[left:right-1]])
#             left += right - left - 1
#             right = left+1

#     return answer

def solution(msg):
    answer = []
    left = 0
    right = 0
    alist = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    ddict = {alist[i]: i+1 for i in range(26)}
    last_val = ddict['Z']
    
    while left < len(msg):
        right = left + 1
        
        while right <= len(msg) and msg[left:right] in ddict:
            right += 1
            
        if right <= len(msg):  
            ddict[msg[left:right]] = last_val+1
            last_val += 1
            
        answer.append(ddict[msg[left:right-1]])
        left = right - 1
        
    return answer
# TOBEORNOTTOBEORTOBEORNOT
# right - 23
# left - 22
# answer - 20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 
# ddict[TO] - 27 / ddict[OB] - 28 / ddict[BE] - 29 / ddict[EO] - 30 / ddict[OR] - 31
# ddict[RN] - 32 / ddict[NO] - 33 / ddict[OT] - 34 / ddict[TT] - 35 / ddict[TOB] - 36
# ddict[BEO] - 37 / ddict[ORT] - 38 / ddict[TOBE] - 39 / ddict[EOR] - 40
# ddict[RNO] - 41 / 