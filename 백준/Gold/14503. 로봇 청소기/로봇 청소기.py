'''
현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
반시계 방향으로 90도 회전한다.
바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
1번으로 돌아간다.
d 0: 북, 1: 동, 2: 남, 3: 서
'''

import sys
inp = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 1
n, m = map(int, inp().split())
r,c,direction = map(int, inp().split())
room = [list(map(int, inp().split())) for _ in range(n)]

room[r][c] = 2

while True:
    mode = False
    # 한 방향이라도 청소할 곳이 남아있으면 끝나지 않음
    for i in range(4):
        direction=(direction+3)%4
        if room[r+dx[direction]][c+dy[direction]]==0:
            mode = True
            room[r][c]=-1
            r=r+dx[direction]
            c=c+dy[direction]
            room[r][c]=2
            cnt+=1
            break
    if mode==False:
        if room[r+dx[(direction+2)%4]][c+dy[(direction+2)%4]]==1:
            print(cnt)
            exit()

        room[r][c] = -1
        r = r+dx[(direction+2)%4]
        c = c+dy[(direction+2)%4]
        room[r][c] = 2