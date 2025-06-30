import heapq

def solution(operations):
    max_heap, min_heap = [], []
    deleted = 0
    for op in operations:
        cmd, val = op.split()
        
        # 명령이 I이면 숫자 삽입
        if cmd == 'I':
            heapq.heappush(max_heap, -int(val))
            heapq.heappush(min_heap, int(val))
            
        # # 명령이 D이면 삭제
        elif cmd == 'D':
            if max_heap and val == '1':
                deleted = -heapq.heappop(max_heap)
                if deleted in min_heap: min_heap.pop(min_heap.index(deleted))
                
            elif min_heap and val == '-1':
                heapq.heappop(min_heap)
        
    if not min_heap: return [0,0]
    
    return [max(min_heap),min(min_heap)]

                