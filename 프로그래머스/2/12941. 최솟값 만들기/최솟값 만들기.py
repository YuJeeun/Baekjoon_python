def solution(A,B):
    answer = 0
    A, B = sorted(A, reverse = True), sorted(B)
    
    for i in range(len(A)):
        answer += A[i]*B[i]
        
    return answer