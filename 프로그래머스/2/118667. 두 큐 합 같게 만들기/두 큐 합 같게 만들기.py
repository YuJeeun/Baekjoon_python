from collections import deque
def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    queue1sum, queue2sum = sum(queue1), sum(queue2)
    ssum = queue1sum + queue2sum
    maxcnt = len(queue1)*2 + 2
    cnt = 0
    
    if ssum % 2 != 0: return -1
    
    while queue1sum != queue2sum:
        if not queue1 or not queue2: return -1
        
        if maxcnt > 0:
            if queue1sum > queue2sum:
                queue1pop = queue1.popleft()
                queue2.append(queue1pop)
                queue2sum += queue1pop
                queue1sum -= queue1pop

            elif queue1sum < queue2sum:
                queue2pop = queue2.popleft()
                queue1.append(queue2pop)
                queue2sum -= queue2pop
                queue1sum += queue2pop
                
            cnt += 1
            maxcnt -= 1
            
        else: return -1
    
    return cnt
        

'''
- 길이가 같은 두개의 큐
- 추출된 원소는 다른 큐에 insert해야함
- pop + insert -> 1회
- 각 큐의 원소의 합을 같게 만들기위해 필요한 작업의 최소 횟수 return
- 각 큐 합을 같게 못만들때는 -1 return
1 <= queue1, queue2 <= 300,000
1 <= queue1, queue2 원소 <= 1e9

[3, 2, 7, 2] [4, 6, 5, 1] 
14 / 16 -> 15 -1 +1 오른쪽에서 1만큼 빠져야함
최소는 빠져야 하는 큐의 맨 앞에 해당 수가 있을 경우

만약에 [1, 2, 3, 4] [2, 3, 4, 5] 10 / 14 24니까 12 1에서는 +2 필요 2에서는 -2 서로 2차이나는 원소 찾기


[1, 2, 1, 2] [1, 10, 1, 2]
6 / 14 -> 10 +4 -4 오른쪽에서 4만큼 빠져야함

[1, 1] [1, 5]
2 / 6 -> 4 +2 -2 오른쪽에서 2만큼 빠져야함

1. 각 큐 합 구하기 -> 14 16 / 6 14 / 2 6 
3. 더 큰쪽에서 부족한 만큼 보내줄 수 있는지 무조건 더 큰쪽에서 보내주면 됨

'''