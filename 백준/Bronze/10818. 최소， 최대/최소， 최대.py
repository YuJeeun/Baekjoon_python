import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))

print(min(numbers), max(numbers))
