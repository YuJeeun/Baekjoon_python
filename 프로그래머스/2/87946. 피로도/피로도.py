maxx = 0 

def solution(k, dungeons):
    global maxx
    dfs(k, [False]*len(dungeons), 0, dungeons)
    return maxx

def dfs(k, visited, cnt, dungeons):
    global maxx
    maxx = max(maxx, cnt)
    for i in range(len(dungeons)):
        min_c, c = dungeons[i]
        if not visited[i] and k >= min_c:
            visited[i] = True
            dfs(k - c, visited, cnt + 1, dungeons)
            visited[i] = False
