def solution(n, words):
    answer = []
    words_set = set()
    words_set.add(words[0])
    for i in range(1, len(words)):
        if words[i-1][-1] == words[i][0]:
            if words[i] not in words_set:
                words_set.add(words[i])
                continue
        p = i//n
        num = i%n
        return [num+1, p+1]
    
    return [0, 0]