'''

3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
'''

T = int(input())
for test_case in range(1, T+1):
    n = input()
    m = input()
    ddict = {}
    n = set(n)
    for i in n:
        ddict[i] = m.count(i)
    print(f'#{test_case}', max(ddict.values()))