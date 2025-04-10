import math
def solution(n, k):
    answer = 0
    num = ''
    num_list = []
    sstr = trans_k(n, k)
    
    for i in range(len(sstr)):
        if sstr[i] == '0':
            if num:
                num_list.append(num)
                num = ''
                
            else:
                continue
        else:
            num += sstr[i]
            
    if num:
        num_list.append(num)
    
    for num in num_list:
        if int(num) == 1:
            continue
        st = is_prime_num(int(num))
        if st:
            answer += 1
            
    return answer

def trans_k(n, k):
    sstr = ''
    while True:
        if n < k:
            sstr+=str(n)
            return sstr[::-1]
    
        sstr += str(n%k)
        n //= k
        
def is_prime_num(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i==0:
            return False
    return True