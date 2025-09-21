from collections import deque
def solution(number):
    cnt = 0
    
    def comb(idx, arr, number):
        nonlocal cnt
        if len(arr) == 3:
            if sum(arr) == 0:
                cnt += 1
            return

        for i in range(idx, len(number)):
            arr.append(number[i])
            comb(i+1, arr, number)
            arr.pop()
    
    comb(0, deque(), number)
    return cnt
    
    
    


# 3명의 정수번호를 더했을 때 0이 되면 삼총사
# 삼총사를 만들수있는 방법의 수 구하기
# 정수번호는 겹칠 수 있음