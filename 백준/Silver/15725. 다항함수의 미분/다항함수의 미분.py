import sys
inp = sys.stdin.readline
polynomial = inp()
if ('x' in polynomial):
    polynomial = polynomial.split('x')
    if(polynomial[0]==''):
        print(1)
    elif(polynomial[0]=='-'):
        print('-1')
    else: print(polynomial[0])
else:
    print(0)
