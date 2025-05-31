def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            if s[i] == '(':
                stack.append(s[i])
            else: return False
        
        elif stack[-1] != s[i]:
            stack.pop()
            
        else: stack.append(s[i])

    if stack: return False

    return True
