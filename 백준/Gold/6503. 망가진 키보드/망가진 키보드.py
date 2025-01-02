import sys
inp = sys.stdin.readline
res = []
while (True):
    m = int(inp().strip())
    if (m==0):
        break
    str = inp().strip()
    chars = [0]*128
    charasci = 0
    maxx, left, curCnt = -1, 0, 0
    for right in range(len(str)):
        charasci = ord(str[right])
        chars[charasci] += 1
        if(chars[charasci]==1): curCnt += 1
        if(curCnt > m):
            if(left < len(str)):    
                charasci = ord(str[left])
                chars[charasci] -= 1
                if(chars[charasci]==0): curCnt -= 1
                left += 1
        maxx = max(maxx, right-left+1)
    res.append(maxx)
for i in range(len(res)):
    print(res[i])

