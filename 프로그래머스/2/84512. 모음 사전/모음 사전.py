from itertools import product
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    wlist = []
    all_word = []
    for i in range(1, 6):
        wlist.append(list(map("".join, product(vowels, repeat = i))))
    for x in wlist:
        for y in x:
            all_word.append(y)
    all_word.sort()
    
    return all_word.index(word)+1



# def solution(word):
#     answer = 0
#     vowels = "AEIOU"
#     wlist = []
#     def words(l, wdict):
#         if l == 5:
#             return
#         for i in range(len(vowels)):
#             wlist.append(wdict+vowels[i])
#             words(l+1, wdict+vowels[i])
        
#     words(0, '')
        
#     return wlist.index(word)+1