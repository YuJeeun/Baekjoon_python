def solution(s):
    stack = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    if stack:
        return 0
    
    return 1


'''
1.같은 알파벳이 2개 붙어있으면 제거
2.앞뒤 이어 붙이기
1,2를 반복하다가 모두 제거되면 return 1
모두 제거가 안되면 return 0

s <= 1,000,000

if stack and stack[-1] == s[i]:
    stack.pop()
else:
    stack.append(s[i]) 
return 1


'''