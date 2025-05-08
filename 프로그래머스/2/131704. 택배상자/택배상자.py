def solution(order):
    result = 0
    main_belt = list(range(len(order), 0, -1))
    sub_belt = []
    idx = 0
    # 5, 4
    # 1, 2, 3
    while main_belt:
        box = main_belt.pop()
        
        if box == order[idx]:
            result += 1
            idx += 1
            
            while sub_belt and sub_belt[-1] == order[idx]:
                sub_belt.pop()
                result += 1
                idx += 1
                
        else:
            sub_belt.append(box)
            
#     while main_belt[-1] != order[0]:
#         box = main_belt.pop()
#         sub_belt.append(box)

#     for i in range(len(order)):
#         if sub_belt and sub_belt[-1] == order[i]:
#             result += 1
#             sub_belt.pop()
            
#         elif main_belt and main_belt[-1] == order[i]:
#             result += 1
#             main_belt.pop()
            
#         else: break
            
    return result

