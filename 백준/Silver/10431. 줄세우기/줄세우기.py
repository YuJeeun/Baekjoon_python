import sys
inp = sys.stdin.readline
p = int(inp())
for _ in range(p):
    arr = list(map(int, inp().split())) # 0번은 테스트케이스 번호
    t = arr[0]
    student = arr[1:]
    cnt = 0
    for i in range(1, len(student)):
        for j in range(i, 0, -1):
            if student[j] < student[j-1]:
                student[j-1], student[j] = student[j], student[j-1]
                cnt += 1
    print(t, cnt)
