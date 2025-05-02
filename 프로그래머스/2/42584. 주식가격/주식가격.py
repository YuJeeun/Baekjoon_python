# def solution(prices):
#     answer = [0]*len(prices)
#     stack = []
    
#     return answer

# [1, 2, 3, 4, 2]
def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i in range(len(prices)):
        if stack:
            if stack[-1][0] <= prices[i]:
                stack.append((prices[i], i))
                
            else:
                while stack and stack[-1][0] > prices[i]:
                    val, idx = stack.pop()
                    answer[idx] = i - idx
                stack.append((prices[i], i))
                
        else: stack.append((prices[i], i))
        
    last_val, last_idx = stack.pop()
    for i in range(len(stack)):
        answer[stack[i][1]] = last_idx - stack[i][1]
    return answer