import sys
inp = sys.stdin.readline

while True:
    ps = inp()
    if ps == '.\n':
        exit()
    stack = []
    for i in range(len(ps)):
        for j in ps[i]:
            if j == '(' or j == '[':
                stack.append(j)
            elif stack and stack[-1] == '(' and j == ')':
                stack.pop()
            elif stack and stack[-1] == '[' and j == ']':
                stack.pop()
            elif j == ')' or j == ']':
                stack.append(j)
                break
    if stack:
        print('no')
    else:
        print('yes')