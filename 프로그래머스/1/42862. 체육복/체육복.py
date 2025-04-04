# def solution(n, lost, reserve):
#     answer = 0

#     for i in range(1, n+1):
#         if i not in lost and i not in reserve:
#             answer += 1
#             continue
        
#         elif i in lost and i in reserve:
#             answer += 1
#             reserve.remove(i)
#             continue 
            
#         if i in reserve:
#             answer += 1
#             continue
            
#         if i in lost:
#             if i-1 in reserve:
#                 answer += 1
#                 reserve.remove(i-1)
#                 continue
                
#             elif i+1 in reserve:
#                 answer += 1
#                 reserve.remove(i+1)
#                 continue
        
#     return answer

'''
*여벌 가져온 학생이 도난당했을 수도 있음->빌려줄수없음
reserve에 있는 애들 중에 도난 당한 있는애 있는지 먼저 확인하고 lost 확인하기

 

        
'''


def solution(n, lost, reserve):
    answer = 0
    visited = [False]*(n+1)
    tmp_list = []
    for r in reserve:
        if r in lost:
            answer += 1
            # reserve.remove(r)
            tmp_list.append(r)
        else:
            answer += 1
            visited[r] = True
    for i in tmp_list:
        reserve.remove(i)
        lost.remove(i)
        visited[i] = True
                
    for i in range(1, n+1):
        if i not in lost and i not in reserve and not visited[i]:
            answer += 1
            continue
        
        if i in lost:
            if i-1 in reserve:
                answer += 1
                reserve.remove(i-1)
                continue
                
            elif i+1 in reserve:
                answer += 1
                reserve.remove(i+1)
                continue       
            
    return answer