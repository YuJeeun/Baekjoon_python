from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    answer = queue(q, location)
    return answer

def queue(q, location):
    cnt = 0
    s = False
    while True:
        val, idx = q.popleft()
        for v, i in q:
            if val < v:
                s = True
        if s:
            q.append((val, idx))
        else:
            cnt += 1
            if location == idx:
                return cnt
        s = False
    
            