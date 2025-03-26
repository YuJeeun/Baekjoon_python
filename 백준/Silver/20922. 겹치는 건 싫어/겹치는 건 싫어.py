import sys
from collections import deque, defaultdict
inp = sys.stdin.readline

n, k = map(int, inp().split())
arr = list(map(int, inp().split()))

queue = deque()

arr_dict = defaultdict(int)

max_len = 0
left = 0
for i in range(n):
    arr_dict[arr[i]] += 1
    while arr_dict[arr[i]] > k:
        arr_dict[arr[left]] -= 1
        left += 1
    max_len = max(max_len, i-left+1)
print(max_len)    

