def solution(sequence, k):
#     answer, mmin = consecutive_sequence(sequence, k)

#     if len(answer) != 1:
#         for val in answer:
#             start, end = val[0], val[1]
#             if mmin == end-start: return [start, end]
            
#     return answer[0]
    answer = consecutive_sequence(sequence, k)
    return answer

# def consecutive_sequence(sequence, k):
#     mmin = int(1e9)
#     result = []

#     if k in sequence: 
#         result.append([sequence.index(k), sequence.index(k)])
#         return result, mmin
    
#     for i in range(len(sequence)-1):
#         start, end = i, i+1
#         total = sequence[start] + sequence[end]
        
#         while True:
#             if mmin <= end-start: break
            
#             if total > k: break
            
#             if total == k:
#                 mmin = end-start
#                 result.append([start, end])
#                 break
            
#             if end == len(sequence)-1: break
            
#             end += 1
#             total += sequence[end]
            
#     return result, mmin

def consecutive_sequence(sequence, k):
    start, end = 0, 0
    total = sequence[0]
    result = [0, len(sequence)]
    while True:
        if total < k:
            end += 1
            if end == len(sequence): break
            total += sequence[end]
        
        else:
            if total == k:
                if end-start < result[1] - result[0]:
                    result = [start, end]
                    
            total -= sequence[start]
            start += 1
            
    return result