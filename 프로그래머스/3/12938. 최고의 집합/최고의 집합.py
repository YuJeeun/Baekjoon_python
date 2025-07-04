def solution(n, s):
    answer = []
    
    if s//n <= 0: return [-1]

    for _ in range(n):
        answer.append(s//n)
    
    r = s%n
    
    for i in range(len(answer)):
        if r == 0: break
        answer[i] += 1
        r -= 1
    
    answer.sort()
    
    return answer