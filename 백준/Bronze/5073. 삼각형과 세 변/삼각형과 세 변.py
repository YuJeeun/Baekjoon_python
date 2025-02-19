import sys
inp = sys.stdin.readline

while True:
    a, b, c = map(int, inp().split())
    if a==0 and b==0 and c==0:
        exit()
    if max(a, b, c) >= (a+b+c - max(a, b, c)):
        print('Invalid')
    elif a==b==c:
        print('Equilateral')

    elif a!=b and b!=c and a!=c:
        print('Scalene')
    else:
        print('Isosceles')
