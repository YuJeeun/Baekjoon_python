def solution(storey): 
    cnt = 0
    while True:
        if storey == 0:
            return cnt
            exit()
            
        ss = storey%10
        if ss < 5:
            cnt += ss
            storey = (storey-ss)//10
            
        elif ss > 5:
            cnt += 10-ss
            storey = (storey+10-ss)//10
            
        elif ss == 5:
            if (storey-ss)//10%10 >= 5:
                cnt += 10-ss
                storey = (storey+10-ss)//10
            else:
                cnt += ss
                storey = (storey-ss)//10
                
        print(cnt, ss, storey)