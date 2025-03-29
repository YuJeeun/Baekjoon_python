from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = bfs(begin, target, words)
    return answer

def bfs(begin, target, words):
    queue = deque()
    queue.append((begin, 0))
    while queue:
        cur, cnt = queue.popleft()
        if cur == target:
            return cnt
        # 단어 list중에 cur랑 비교해서 하나만 다른게 있는지
        for word in words:
            count = 0
            for i in range(len(word)):
                if cur[i] == word[i]:
                    continue
                count += 1
            
            if count == 1: # 하나만 다르면 queue에 넣기
                queue.append((word, cnt+1))
    return 0
    