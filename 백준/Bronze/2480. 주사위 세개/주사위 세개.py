# 3개 10000 + (같은 눈) * 1000
# 2개 1000 + (같은 눈) * 100
# 없음 (가장 큰 눈) * 100

a,b,c=map(int,input().split())
result=0
if(a==b==c):
    result=10000+(a*1000)
elif(a==b or b==c or a==c):
    if(a==b):
        result=1000+(a*100)
    elif(b==c):
        result=1000+(b*100)
    elif(a==c):
        result=1000+(a*100)
else:
    result=max(a,b,c)*100

print(result)