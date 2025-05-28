def solution(numbers):
    answer = 0
    num = ''
    num_set = set()
    visited = [False]*(len(numbers)+1)
    
    def isprime(num):
        if not num or num in ('0', '1'):
            return False       
        num = int(num)
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False 
        return True
    
    def dfs():
        nonlocal num, num_set
        nonlocal answer
        
        if num:
            num_set.add(int(num))        

        for i in range(len(numbers)):
            if visited[i]: continue
            num += numbers[i]
            visited[i] = True
            dfs()
            num = num[:len(num)-1]
            visited[i] = False
            
    dfs()    
    
    for number in num_set:
        if isprime(number):
            answer += 1
    return answer


'''
0 1 1
0, 1, 01, 10, 11, 
'''