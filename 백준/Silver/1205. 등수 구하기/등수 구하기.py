import sys
inp = sys.stdin.readline

n, score, p = map(int, inp().split())
if n == 0:
    print(1)
    exit()

ranking_list = list(map(int, inp().split()))
# ranking_list = [-x for x in ranking_list]
# score = score*(-1)
# ranking_list.append(score)
# for i in range(1, len(ranking_list)):
#     for j in range(i, 0, -1):
#         if ranking_list[i] < ranking_list[i-1]:
#             ranking_list[i-1], ranking_list[i] = ranking_list[i], ranking_list[i-1]
#         else:
#             break
# if len(ranking_list)-1 != p:
#     print(ranking_list.index(score)+1)

# else:
#     if ranking_list[-1] == score:
#         print(-1)
#     else:
#         print(ranking_list.index(score)+1)

ranking_list.append(score)
ranking_list.sort()
ranking_list=list(reversed(ranking_list))
if len(ranking_list)-1 != p:
    print(ranking_list.index(score)+1)  
else:
    if ranking_list[-1] == score:
        print(-1)
    else:
        print(ranking_list.index(score)+1)  
        