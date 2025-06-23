def solution(n):
    answer = []
    nx, ny = 0, 0
    dx, dy = [1, 0, -1], [0, 1, -1]
    idx, cnt, ll = 0, 2, 0
    appended = [[-1]*i for i in range(1, n+1)]

    for i in range(len(appended)):
        ll += len(appended[i])
    
    appended[0][0] = 1
    
    while True:
        if cnt > ll: break
    
        nx, ny = nx+dx[idx], ny+dy[idx]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or appended[nx][ny] != -1:
            nx, ny = nx-dx[idx], ny-dy[idx]
            idx = (idx+1)%3
            continue
        
        appended[nx][ny] = cnt
        cnt += 1
    
    for i in range(len(appended)):
        for j in range(len(appended[i])):
            answer.append(appended[i][j])
    
    return answer
'''
0,0 1
1,0 2
2,0 3
3,0 4
3,1 5
3,2 6
3,3 7
2,2 8
1,1 9
2,1 10

[1, 0, -1]
[0, 1, -1]

'''