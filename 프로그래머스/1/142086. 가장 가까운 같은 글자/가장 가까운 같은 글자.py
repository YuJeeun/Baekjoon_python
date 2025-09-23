def solution(s):
    answer = []
    sdict = dict()
    for i in range(len(s)):
        if s[i] in sdict:
            answer.append(i-sdict[s[i]])
            sdict[s[i]] = i
        else: 
            answer.append(-1)
            sdict[s[i]] = i
    return answer