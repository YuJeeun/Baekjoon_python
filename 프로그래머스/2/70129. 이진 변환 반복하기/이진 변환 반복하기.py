def solution(s):
    answer = []
    cnt, zero = procedure(s)
    return cnt, zero

def procedure(s):
    cnt = 0
    total_zero = 0
    while True:
        cnt += 1
        zero = s.count('0')
        one = len(s) - zero
        s = format(one, 'b')
        total_zero += zero
        if s == '1':
            return cnt, total_zero