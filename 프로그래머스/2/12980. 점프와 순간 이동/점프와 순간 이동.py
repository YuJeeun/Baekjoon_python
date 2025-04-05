answer = 0
def solution(n):
    global answer
    answer = used(n)
    
    return answer
'''
1: +k, 2: (현재까지온거리)*2
1의 경우 건전지 사용
2의 경우 X
이동하려는 거리 N이 주어졌을 때 사용해야하는 건전지 사용량의 최솟값 return

점프는 한번에 n까지 가능 0에서 (1, 2, 3, ... , n) 점프 (n만큼 건전지 사용)
1 <= k, n <= 1,000,000,000
'''
def used(n): 
    if n == 1:
        return 1
    if n%2 == 0:
        return used(n//2)
    else:
        return used(n-1)+1