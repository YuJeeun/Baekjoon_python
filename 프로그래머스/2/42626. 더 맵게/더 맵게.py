import heapq

def solution(scoville, K):
    answer = scovilles(scoville, K)
    return answer

def scovilles(scoville, k):
    queue = []
    cnt = 0
    for i in scoville:
        heapq.heappush(queue, i)
    while True:
        if all(i >= k for i in queue):
            return cnt
        
        if len(queue) < 2:
            return -1
        
        cnt += 1
        least_spicy = heapq.heappop(queue)
        next_least_spicy = heapq.heappop(queue)
        new_food = least_spicy+(next_least_spicy*2)
        heapq.heappush(queue, new_food)

'''
스코빌 지수가 k 이상이 될 때까지 반복하여 섞기
모든 음식의 스코빌 지수가 k이상이 되는 최소 횟수 return
안될 경우 -1 return
'''    