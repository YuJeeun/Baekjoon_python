def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    cnt = 0
    for i in range(len(B)):
        if A[cnt] < B[i]:
            answer += 1
            cnt += 1
    return answer