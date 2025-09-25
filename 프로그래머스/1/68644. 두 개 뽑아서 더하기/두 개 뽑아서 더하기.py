def solution(numbers):
    sset = set()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            sset.add(numbers[i]+numbers[j])
            
    sset = list(sset)
    sset.sort()
    return sset