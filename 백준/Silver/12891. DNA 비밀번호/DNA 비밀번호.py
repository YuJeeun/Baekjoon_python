import sys
from collections import deque
inp = sys.stdin.readline

p, s = map(int, inp().split())
dna = inp()
acgt = list(map(int, inp().split()))
acgt_cnt = {'A':0, 'C': 0, 'G': 0, 'T': 0}
cnt = 0
queue = deque()

for i in range(p):
    queue.append(dna[i])
    acgt_cnt[dna[i]] += 1
    if len(queue) == s:
        if acgt_cnt['A'] < acgt[0] or acgt_cnt['C'] < acgt[1] or acgt_cnt['G'] < acgt[2] or acgt_cnt['T'] < acgt[3]: 
            val = queue.popleft()
            acgt_cnt[val] -= 1
        else:
            cnt += 1
            val = queue.popleft()
            acgt_cnt[val] -= 1
print(cnt)