'''
올바른 수식 만들기
1. 수식은 ㅁㅁ+ㅁㅁ=ㅁㅁ 향테 0~9
2. 모든 수는 항상 두자릿수
3. '+', '='도 각각 두 개의 성냥개비 필요
'''

# N개의 성냥개비가 주어졌을 때, 성냥을 모두 사용하여 조건을 만족하는 수식을 만들 수 있는가
# 가능한 답이 없다면 impossible 출력
# 가능한 답이 여러 개인 경우 그 중 하나를 출력

import sys
inp = sys.stdin.readline

n = int(inp())-4
number = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
result = []
a1=0
a2=0
b1=0
b2=0
c1=0
c2=0
for a in range(100):
    for b in range(100):
        if(a+b<100):
            a1=a//10
            a2=a%10
            b1=b//10
            b2=b%10
            c1=(a+b)//10
            c2=(a+b)%10
            if(n==(number[a1]+number[a2]+number[b1]+number[b2]+number[c1]+number[c2])):
                result.append(f'{a1}{a2}+{b1}{b2}={c1}{c2}')
if (result==[]):
    print('impossible')
else:
    print(result[0])