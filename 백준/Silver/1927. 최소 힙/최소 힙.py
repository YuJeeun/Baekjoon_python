import sys
import heapq
inp = sys.stdin.readline

n = int(inp())
queue = []

for _ in range(n):
    x = int(inp())
    if x == 0:
        if queue:
            print(heapq.heappop(queue))
        else:
            print(0)
        continue
    heapq.heappush(queue, x)