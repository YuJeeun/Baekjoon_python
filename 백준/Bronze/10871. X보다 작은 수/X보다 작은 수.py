#N개의 수열A, 정수 X
#X보다 작은 수만 입력받은 순서대로 출력

N,X = map(int,input().split())
A=list(map(int,input().split()))
result=[]
for i in range(N):
    if A[i]<X:
        result.append(A[i])
print(' '.join(map(str,result)))