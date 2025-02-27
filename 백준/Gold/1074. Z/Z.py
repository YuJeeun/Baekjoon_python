import sys
inp = sys.stdin.readline

n, r, c = map(int, inp().split())

def z(n, r, c):
    if n == 0:
        return 0

    else:
        # 1사분면이면: return n-1크기*0 + n-1의 r%2, c%2
        if r//pow(2, n-1) == 0 and c//pow(2, n-1) == 0:
            return z(n-1, r%pow(2, n-1), c%pow(2, n-1))
        # 2사분면이면: return n-1의 크기*1 + n-1의 r%2, c%2
        elif r//pow(2, n-1) == 0 and c//pow(2, n-1) == 1:
            return (pow(2, n-1)*pow(2, n-1)) + z(n-1, r%pow(2, n-1), c%pow(2, n-1))
        # 3사분면이면: return n-1의 크기*2 + n-1의 r%2, c%2
        elif r//pow(2, n-1) == 1 and c//pow(2, n-1) == 0:
            return (pow(2, n-1)*pow(2, n-1)) * 2 + z(n-1, r%pow(2, n-1), c%pow(2, n-1))
        # 4사분면이면: return n-1의 크기*3 + n-1의 r%2, c%2
        elif r//pow(2, n-1) == 1 and c//pow(2, n-1) == 1:
            return (pow(2, n-1)*pow(2, n-1)) * 3 + z(n-1, r%pow(2, n-1), c%pow(2, n-1))

print(z(n, r, c))