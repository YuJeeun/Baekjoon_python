def solution(prices):
    answer = [0]*len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack and stack[-1][0] > prices[i]:
            _, idx = stack.pop()
            answer[idx] = i - idx
        stack.append((prices[i], i))
    
    _, last_idx = stack.pop()

    for i in range(len(stack)):
        answer[stack[i][1]] = last_idx - stack[i][1]
        
    return answer