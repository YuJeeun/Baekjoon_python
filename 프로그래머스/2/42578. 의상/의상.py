def solution(clothes):
    answer = combi(clothes)
    return answer

'''
서로 다른 옷의 조합 수 return
최소 하나 이상은 입어야함
1개만 입는 경우 - 전체 옷 개수
headgear - yellow_hat, green_turban
eyewear - blue_sunglasses
-> 1개만 입는 경우 3, 2개 입는 경우 2c2 = 2*1/2*1*0 = 1 / 1*2개 
face - crow_mask, blue_sunglasses, smoky_makeup
-> 1개만 입는 경우 3
headgear - yellow_hat, green_turban
eyewear - blue_sunglasses
face - 1, 2, 3, 4
1개만 입는 경우 - 7 2개 입는 경우 - 14 3개 입는 경우 - 8개=> 29
'''
def combi(clothes):
    ddict = {}
    combi = 1
    for i in range(len(clothes)):
        if clothes[i][1] in ddict:
            ddict[clothes[i][1]] += 1
        else:
            ddict[clothes[i][1]] = 1
    for value in ddict.values():
        combi *= value+1
    return combi-1
    
    