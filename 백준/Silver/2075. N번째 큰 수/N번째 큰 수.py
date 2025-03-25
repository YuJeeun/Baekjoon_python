import sys
import heapq

inp = sys.stdin.readline

n = int(inp())

queue = []

for _ in range(n):
    for num in map(int, inp().split()):
        if len(queue) < n:
            heapq.heappush(queue, num)
        else:
            if queue[0] < num:
                heapq.heappushpop(queue, num)
print(queue[0])