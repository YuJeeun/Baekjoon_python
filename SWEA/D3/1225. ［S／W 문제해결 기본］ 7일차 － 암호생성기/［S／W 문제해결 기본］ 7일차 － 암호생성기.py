from collections import deque

for test_case in range(1, 11):
    _ = int(input()) # 이건 도대체 왜주는거지
    numbers = deque(list(map(int, input().split())))

    while True:
        for i in range(1, 6):
            num = numbers.popleft()
            num = num - i
            if num <= 0:
                num = 0
                numbers.append(num)
                break

            numbers.append(num)
        if 0 in numbers:
            break

    print(f'#{test_case}', *numbers)