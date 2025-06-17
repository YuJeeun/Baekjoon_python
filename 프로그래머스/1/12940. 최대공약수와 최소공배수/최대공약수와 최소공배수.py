def solution(n, m):
    answer = []
    answer.append(GCD(n, m))
    answer.append(LCM(n, m))
    return answer

# 최대공약수
def GCD(n, m):
    maxx, minn = max(n, m), min(n, m)
    
    while minn > 0:
        maxx, minn = minn, maxx%minn
    
    return maxx

# 최소공배수
def LCM(n, m):
    return n*m / GCD(n, m)
