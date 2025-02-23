import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp())

board = []
for i in range(n):
    board.append(list(inp().strip()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

h_coor = []
def find_heart():
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                heart_x = i+1
                heart_y = j
                board[i][j] = -1
                board[heart_x][heart_y] = -1
                return heart_x+1, heart_y+1

def bfs():
    for i in range(n):
        for j in range(n):
            queue = deque()
            if board[i][j] == '*':
                board[i][j] = -1
                queue.append((i, j, 1))
                while queue:
                    cur_x, cur_y, length = queue.popleft()
                    for k in range(4):
                        nx = dx[k] + cur_x
                        ny = dy[k] + cur_y
                        if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] != '*': continue
                        board[nx][ny] = -1
                        queue.append((nx, ny, length+1))
                print(length, end= ' ')   

h_coor.append(find_heart())
print(h_coor[0][0], h_coor[0][1])
bfs()