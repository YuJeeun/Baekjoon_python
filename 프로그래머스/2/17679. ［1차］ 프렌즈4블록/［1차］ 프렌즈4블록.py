def solution(m, n, board):
    answer = 0
    del_val = set()
    total = 0
    arr = [[0]*n for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            arr[i][j] = board[i][j]
            
    while True:  
        status, arr = del_block(arr, m, n, del_val)
        if not status:
            return total
            exit()
        arr = pull_down(arr, m, n)
        total += len(del_val)
        del_val.clear()
    
def del_block(arr, m, n, del_val):
    for i in range(m-1):
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1] == arr[i+1][j] == arr[i+1][j+1] and arr[i][j] != '0':
                del_val.add((i,j))
                del_val.add((i,j+1))
                del_val.add((i+1,j))
                del_val.add((i+1,j+1))
                
    if not del_val: # 삭제할 블록이 없다면
        return False, arr
    
    for (i, j) in del_val:
        arr[i][j] = '0'
        
    return True, arr

def pull_down(arr, m, n):
    for i in range(m-1):
        for j in range(n):
            p = i
            while 0 <= p and arr[p][j].isalpha() and arr[p+1][j] == '0':
                arr[p][j], arr[p+1][j] = arr[p+1][j], arr[p][j]
                p -= 1
    return arr
'''
[['0', '0', '0', 'A', '0', '0'],
['0', '0', '0', 'A', '0', '0'],
['T', '0', 'T', 'F', 'N', 'T'], 
['T', 'T', 'F', 'R', 'A', 'A'],
['T', 'T', 'M', 'M', 'M', 'F'], 
['T', 'M', 'M', 'T', 'T', 'J']]
'''