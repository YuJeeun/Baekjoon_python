'''
n: 엠티에 참가한 사람 수(1~n) 선영이가 1
e: 일차 (1~50)
k: 그 날 참가한 사람의 수 (2~n)
* 선영이는 적어도 한 번 캠프파이어에 참가함
'''

# MT가 끝났을 때 선영이를 포함해 모든 노래를 아는 사람의 번호를 오름차순으로 출력하기

import sys
inp = sys.stdin.readline
n = int(inp())
e = int(inp())

arr = [set(list(map(int, inp().strip().split()))[1:]) for _ in range(e)]
# 노래 개수
# 노래를 모두 아는 사람
# 각자 아는 노래

# 일차만큼 반복
# 선영이(1)가 있다면 노래 개수 +1, 참가한 사람들을 키로 가지는 dict의 value에 cnt 추가
# 선영이가 없다면 노래 개수 그대로, 전날 참가한 사람이 있으면 value에 cnt 추가
# 모든 일정이 끝나고 노래의 개수와 아는 노래의 개수가 같은 사람들만 result에 추가 후 출력

song_cnt = 0
songs = {person: set() for person in range(1, n + 1)}
for day in range(e):
    if (1 in arr[day]):
        song_cnt+=1
        for person in arr[day]:
            songs[person].add(song_cnt)
    else:
        known_songs = set()
        for person in arr[day-1]:
            known_songs.update(songs[person])
        for person in arr[day]:
            if(any(p for p in arr[day-1])):
                songs[person].update(known_songs)
for person in range(1,n+1):
    if(song_cnt==len(songs[person])):
        print(person)