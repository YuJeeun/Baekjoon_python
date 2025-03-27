def solution(s):
    answer = stack(s)
    return answer

def stack(s):
    ddict = {')': '(', ']': '[', '}': '{'}
    cnt = 0
    n = 0
    while n < len(s):
        stack = []
        strr = s[n:] + s[:n]
        for i in range(len(strr)):
            if strr[i] == '(' or strr[i] == '[' or strr[i] == '{':
                stack.append(strr[i])
                continue
            elif stack and stack[-1] == ddict[strr[i]]:
                stack.pop()
                continue
            else:
                stack.append(s[i])
                break
        if not stack:
            cnt += 1
        n += 1
    return cnt
    
