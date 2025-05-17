'''
1 <= n <= 100,000
1 <= m <= 100,000
사이트 주소 비밀번호 출력하기
'''

n, m = map(int, input().split())
ddict = {}
for i in range(n):
    site, pw = input().split()
    ddict[site] = pw

sites= [input() for _ in range(m)]

for i in range(m):
    print(ddict[sites[i]])