from collections import defaultdict
def solution(s):
    answer = result(s)
    return answer

# def result(str):
#     ddict = defaultdict(int)
#     llist = ''
#     for s in str:
#         if s == '{' or s == '}' or s == ',':
#             if not llist:
#                 continue
#             else:
#                 ddict[int(llist)] += 1
#                 llist = ''
#         else:
#             llist += s
    
#     result = [0]*len(ddict)
#     for key, value in ddict.items():
#         result[len(ddict)-value] = key

#     return result

def result(str):
    result = []
    str = str.lstrip('{').rstrip('}').split('},{')
    new_s = []
    for i in str:
        new_s.append(i.split(','))
    new_s.sort(key = len)

    for i in range(len(new_s)):
        for s in new_s[i]:
            if int(s) not in result:
                result.append(int(s))
    return result
    
                      