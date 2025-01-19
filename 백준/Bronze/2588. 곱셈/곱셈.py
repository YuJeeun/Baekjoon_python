a = int(input())
b = int(input())

line1 = a * (b % 10)       
line2 = a * ((b // 10) % 10) 
line3 = a * (b // 100)       
result = a * b              

print(line1)
print(line2)
print(line3)
print(result)
