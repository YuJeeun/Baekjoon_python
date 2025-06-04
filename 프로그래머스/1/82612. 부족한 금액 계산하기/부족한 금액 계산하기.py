def solution(price, money, count):
    total = 0
    for i in range(1, count+1):
        total += i*price
    return total-money if total > money else 0
