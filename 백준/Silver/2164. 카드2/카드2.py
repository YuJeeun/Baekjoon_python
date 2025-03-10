import sys
from collections import deque
inp = sys.stdin.readline

n = int(inp())
cards = deque()
llist = [x for x in range(1, n+1)]
for card in llist:
    cards.append(card)
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards.pop())