def solution(brown, yellow):
    answer = []
    answer = carpet(brown, yellow)
    return answer

def carpet(brown, yellow):
    for i in range(1, yellow+1):
        if yellow%i == 0:
            w = i
            l = yellow//i
            if w < l:
                continue
            if (w+2)*(l+2) == brown+yellow:
                return [w+2, l+2]