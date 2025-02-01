# import sys

# inp = sys.stdin.readline

# r, c = map(int, inp().split())

# board = [inp().strip() for _ in range(r)]

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# visit = set()

# max_count = 0

# def dfs(x, y, count):
#     global max_count
#     max_count = max(max_count, count)
#     for i in range(4):
#         nx = dx[i] + x
#         ny = dy[i] + y
#         if nx < 0 or ny < 0 or nx >= r or ny >= c or board[nx][ny] in visit: continue
#         visit.add(board[nx][ny])
#         dfs(nx, ny, count+1)
#         visit.remove(board[nx][ny])

# visit.add(board[0][0])
# dfs(0, 0, 1)
# print(max_count)


import sys

inp = sys.stdin.readline

r, c = map(int, inp().split())

board = [inp().strip() for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visit = [[False] * c for _ in range(r)]

alphabet = [False] * 26

max_count = 0

def dfs(x, y, count):
    global max_count
    max_count = max(max_count, count)
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or ny < 0 or nx >= r or ny >= c or visit[nx][ny] or alphabet[ord(board[nx][ny]) - 65]: continue
        visit[nx][ny] = True
        alphabet[ord(board[nx][ny]) - 65] = True
        dfs(nx, ny, count+1)
        visit[nx][ny] = False
        alphabet[ord(board[nx][ny]) - 65] = False

visit[0][0] = True
alphabet[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)
print(max_count)
