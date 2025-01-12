n, m = map(int, input().split())
matrix_a = []  
matrix_b = []  

for _ in range(n):
    matrix_a.append(list(map(int, input().split())))

for _ in range(n):
    matrix_b.append(list(map(int, input().split())))

result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)

for row in result:
    print(" ".join(map(str, row)))
