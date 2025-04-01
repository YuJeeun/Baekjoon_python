def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    str1_dict, str2_dict = append_dict(str1, str2)
    
    if not (str1_dict or str2_dict) : 
        return 65536
    
    str_intersection = 0 
    str_union = 0
    
    for key, value in str1_dict.items():
        if key in str2_dict.keys():
            str_intersection += min(value, str2_dict[key])
            str_union += max(value, str2_dict[key])
        else:
            str_union += value
            
    for key, value in str2_dict.items():
        if key not in str1_dict.keys():
            str_union += value
    
    return int((str_intersection/str_union)*65536)
    
    
    
    
def append_dict(str1, str2):
    str1_dict, str2_dict = {}, {}
    
    for i in range(len(str1)-1):
        if (str1[i]+str1[i+1]).isalpha():
            if str1[i]+str1[i+1] in str1_dict:
                str1_dict[str1[i]+str1[i+1]] += 1
            else:
                str1_dict[str1[i]+str1[i+1]] = 1
    
    for i in range(len(str2)-1):
        if (str2[i]+str2[i+1]).isalpha():
            if str2[i]+str2[i+1] in str2_dict:
                str2_dict[str2[i]+str2[i+1]] += 1
            else:
                str2_dict[str2[i]+str2[i+1]] = 1
            
    return str1_dict, str2_dict
'''
2 <= str1, str2 <= 1,000
입력으로 들어온 두 문자열의 자카드 유사도 출력 int(유사도*65536)
두글자씩 끊어서 다중 집합의 원소로 만듦
영문쌍만 유효 -> isalpha() true 인것만
false면 저장X
대소문자 차이 무시하므로 upper()

HA AN ND DS SH HA AK KE / SH HA AK KE HA AN ND DS
교집합 - HA HA AN ND DS SH AK KE
합집합 - HA HA AN ND DS SH AK KE
HA: 2
AN: 1
ND: 1
DS: 1
SH: 1
AK: 1
KE: 1
------
HA: 2
AN: 1
ND: 1
두 딕셔너리 사이에 모두 있는 key인가 -> 맞다면 그 중 더 작은 값 (교)
1 -> 65536

AA AA / AA AA AA
교집합 - AA AA 
합집합 - AA AA AA
2/3 -> 43690


'''
