def solution(orders, course):
    global ddict
    for i in range(len(orders)):
        orders[i] = sorted(orders[i])
        for c in course:
            comb(0, orders[i], c)
    # ddict에서 value가 0인거 지우기
    # key의 길이가 같은 것 중에 제일 많은거만 남기고 지우기
    ddict = {k: v for k, v in ddict.items() if v != 0}
    key_group = {}
    for key, value in ddict.items():
        if len(key) not in key_group:
            key_group[len(key)] = []
        key_group[len(key)].append((key, value))
    
    result = []
    for key, value in key_group.items():
        max_value = max(value, key = lambda x:x[1])[1]
        for k, v in value:
            if v == max_value:
                result.append(k)
    result = sorted(result)
    return result

'''
1. 주문한 단품메뉴 조합으로 나올 수 있는 조합 다 찾기
2. 2이상부터 dict에 넣기
3. 만약 이미 dict에 있는 조합이면 +1
4. 메뉴 구성 개수가 같은데 더 많이 주문된 메뉴 구성이 있으면 그 메뉴 구성이 코스요리 후보
5. 메뉴 구성 개수도 같고 주문 수도 같으면 다 넣음
요소, 배열 사전순 오름차순 정렬
'''
# AB, AC, AF, AG, BC, BF, -> 일반 조합
s = ''
ddict = {}
def comb(idx, orders, c):
    global s
    if len(s) == c:
        if s not in ddict:
            ddict[s] = 0
        else:
            ddict[s] += 1
    for i in range(idx, len(orders)):
        s += orders[i]
        comb(i+1, orders, c)
        s = s[:len(s)-1]
