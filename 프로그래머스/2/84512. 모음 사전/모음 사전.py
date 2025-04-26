def solution(word):
    answer = 0
    vowels = "AEIOU"
    wlist = []
    def words(l, wdict):
        if l == 5:
            return
        for i in range(len(vowels)):
            wlist.append(wdict+vowels[i])
            words(l+1, wdict+vowels[i])
        
    words(0, '')
        
    return wlist.index(word)+1