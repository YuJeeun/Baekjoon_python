def solution(word):
    answer = 0
    wlist = []
    vowels = "AEIOU"
    w = ''
    def dfs(l, w):
        if l == 5:
            return
        for i in range(len(vowels)):
            wlist.append(w+vowels[i])
            dfs(l+1, w+vowels[i])
    dfs(0, '')
    return wlist.index(word)+1

    