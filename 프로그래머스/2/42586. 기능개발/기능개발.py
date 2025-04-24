from collections import deque

def solution(progresses, speeds):
    answer = []
    done = deque()
    day = 0
    for i in range(len(progresses)):
        day = 0
        while True:
            day += 1
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                done.append(day)
                break
    cnt = 1
    progress = done.popleft()
    
    while True:
        if done:
            if progress >= done[0]:
                done.popleft()
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 1
                if done:
                    progress = done.popleft()
                else:
                    break
        else:
            answer.append(cnt)
            break
    
    return answer


'''
7 3 9
5 10 1 1 20 1
progresses <= 100
day = 0
for i in range(len(progresses)):
    day = 0
    while True:
    day += 1
    progresses[i] += speed[i]
        if progresses[i] >= 100:
            done.append(day)
            continue
'''