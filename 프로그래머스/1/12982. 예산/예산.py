def solution(d, budget):
    answer = 0
    d.sort();
    for i in range(len(d)):
        if(answer+d[i]) > budget:
            return i
        else:
            answer+=d[i]
    return len(d)
