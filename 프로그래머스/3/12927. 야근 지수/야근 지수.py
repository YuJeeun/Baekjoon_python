import heapq

def solution(n, works):
    answer = 0
    max_heap = []
    
    for work in works:
        heapq.heappush(max_heap, -work)
    
    if sum(works) <= n: return 0

    while n != 0:
        n -= 1
        mmax = -heapq.heappop(max_heap)
        mmax -= 1
        heapq.heappush(max_heap, -mmax)
    
    for val in max_heap:
        answer += (-val)**2
        
    return answer