def solution(n, t, m, p):
    answer = ''
    i, cnt = 0, 0
    while len(answer) < t:
        converted = conversion(i, n)
        
        for ch in converted:
            cnt += 1
            
            if cnt % m == p % m:
                answer += ch
                
            if len(answer) == t:
                break
        i += 1
        
    return answer

def conversion(i, n):
    if i==0:
        return '0'

    digits = []
    while i:
        digits.append(int(i % n))
        i //= n
    return ''.join(str(x if x < 10 else chr(x - 10 + ord('A'))) for x in digits[::-1])


# cnt = 0
# def solution(n, t, m, p):
#     answer = ''
#     i = 0
#     while len(answer) < t:
#         answer += conversion(i, n, m, p)
        
#     return answer

# def conversion():
#     global cnt
#     if cnt % m == (p-1):
#         if 10 <= i <= 15:
#             cnt += 1
#             return hex(i)[2:].upper()

#         while x > n-1:
#             y += str(x%n)
#             x = x//n
            
#         y += str(x)  
#         cnt += len(y)
#         y = y[-1::-1]
#         if len(y) == 1:
#             return y
#         return ''.join([y[s] for s in range(len(y)) if s % m == (p - 1)])

#     cnt += 1
#     return y