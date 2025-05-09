'''
1<=n<=10
3
123
894
765

4
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
3: [(0,0) -> (0,1) -> (0,2)] | [(1,2) -> (2,2)] | [(2,1) -> (2,0)] | [(1,0)] | [(1,1)]
4: [(0,0) -> (0,1) -> (0,2) -> (0,3)] | [(1,3) -> (2,3) -> (3,3)] | [(3,2) -> (3,1) -> (3,0)] | [(2,0) -> (1,0)] | [(1,1) -> (1,2)] | [(2,2)] | [(2,1)]

x 유지 y +1 / x +1 y 유지 / x 유지 y -1 / x -1  y 유지 / x 유지 y +1 / 반복
x 유지 y +1 / x +1 y 유지 / x 유지 y -1 / x -1 y 유지 / x 유지 y +1 / x +1 y 유지/ x 유지 y -1

* 이미 방문한 곳은 방문할 수 없음
'''
T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]	# 우, 하, 좌, 상
    direction = 0	# 0: 우, 1: 하, 2: 좌, 3: 상
    nx, ny = 0, 0
    arr[0][0] = 1
    for i in range(2, (n*n)+1):
        nx += dx[direction]
        ny += dy[direction]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] != 0:	# 방문한적이 있거나 방향전환을 해야할 때
            nx -= dx[direction]
            ny -= dy[direction]
            direction = (direction+1)%4
            nx += dx[direction]
            ny += dy[direction]
            arr[nx][ny] = i
            
        else: # 그게 아니라면 숫자 넣고 방문처리
            arr[nx][ny] = i
    print(f'#{test_case}')
    for i in range(n):
        print(*arr[i])
        
        
                


                
                
                
            
            
                    
	    