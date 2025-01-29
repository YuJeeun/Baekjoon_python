import sys

inp = sys.stdin.readline

r, c = map(int, inp().split())

board = [inp().strip() for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def dfs(x, y, bitmask, count): # visit 대신 vitmask 사용 A는 0, B는 1, ...
    global result
    result = max(result, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
        next_char = board[nx][ny]
        next_bit = 1 << (ord(next_char) - ord('A'))

        if bitmask & next_bit:
            continue

        dfs(nx, ny, bitmask | next_bit, count+1)

start_char = board[0][0]
start_bitmask = 1 << (ord(start_char) - ord('A'))
dfs(0,0,start_bitmask,1)

print(result)