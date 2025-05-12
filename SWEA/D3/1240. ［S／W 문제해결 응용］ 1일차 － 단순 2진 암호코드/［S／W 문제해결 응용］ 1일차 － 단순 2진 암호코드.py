T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    cipher = [input() for _ in range(n)]
    ddict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
             '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    for i in range(n):
        if '1' not in cipher[i]: continue
        for j in range(len(cipher[i])):
            if cipher[i][j] == '1':
                x, y = i, j
        break

    fx, fy = x, y-55
    encrypt_num = ''
    decrypt_num = []
    for i in range(0,56,7):
        for j in range(i, i+7):
            encrypt_num += cipher[fx][fy+j]
        decrypt_num.append(ddict[encrypt_num])
        encrypt_num = ''

    even, odd = 0, 0
    for i in range(8):
        if i % 2 == 0:
            odd += decrypt_num[i]
        else:
            even += decrypt_num[i]

    result = odd*3+even

    if result % 10 == 0:
        result = sum(decrypt_num)
        print(f'#{test_case}', result)
    else:
        print(f'#{test_case}', 0)




