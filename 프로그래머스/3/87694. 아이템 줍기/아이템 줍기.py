from collections import defaultdict, deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    new_rectangle = [[0]*4 for _ in range(len(rectangle))]
    for idx, value in enumerate(rectangle):
        for i in range(len(value)):
            new_rectangle[idx][i] = value[i]*2
    area = []
    area = making_area(new_rectangle)

    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2
    answer = bfs(area, characterX, characterY, itemX, itemY)
    
    return answer

def making_area(rectangle):
    max_x = max(max(rec[0], rec[2]) for rec in rectangle)+1
    max_y = max(max(rec[1], rec[3]) for rec in rectangle)+1
    
    area = [[0]*max_y for _ in range(max_x)]
    
    for r in rectangle:
        x1, y1, x2, y2 = r
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                area[i][j] = 1
                
    for r in rectangle:
        x1, y1, x2, y2 = r
        for i in range(x1+1,x2):
            for j in range(y1+1,y2):
                area[i][j] = 0
    

    return area

def bfs(area, characterX, characterY, itemX, itemY):
    n = len(area)
    m = len(area[0])

    queue = deque()
    queue.append((characterX,characterY,1))
    visited = set()
    visited.add((characterX, characterY))
    while queue:
        cur_x, cur_y, cnt = queue.popleft()
        if cur_x == itemX and cur_y == itemY:
            return (cnt//2)
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or area[nx][ny] == 0 or (nx, ny) in visited: continue
            queue.append((nx, ny, cnt+1))
            visited.add((nx, ny))
            
           
         
            
    
    
                