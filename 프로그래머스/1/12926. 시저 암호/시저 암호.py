def solution(s, n):
    answer = ''
    p = 0
    
    for i in range(len(s)):
        p = ord(s[i])+n 
        if ord(s[i]) in range(65, 91):
            answer += chr((p-65)%26+65)
        elif ord(s[i]) in range(97,123):
            answer += chr((p-97)%26+97)
        else:
            answer += ' '
        
    return answer