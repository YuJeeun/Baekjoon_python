def solution(diffs, times, limit):
    start = 1
    end = max(diffs)
    mid = (start+end)//2
    while start <= end:
        result = puzzle(diffs, times, limit, mid)
        if result:
            end = mid -1
        else:
            start = mid + 1
        mid = (start+end)//2
    return mid+1

        
def puzzle(diffs, times, limit, level):
    result = 0
    total_time = 0
    for i in range(len(diffs)):
        if level >= diffs[i]:
            total_time += times[i]
        elif i == 0:
            total_time += times[i]*(diffs[i]-level)+times[i]
        else:
            total_time += (times[i]+times[i-1])*(diffs[i]-level)+times[i]
    result = total_time
    if result > limit:
        return False
    else:
        return True
    

