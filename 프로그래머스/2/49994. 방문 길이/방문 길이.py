def solution(dirs):
    answer = 0
    cur_x, cur_y = 0, 0
    llist = [('U', 0, 1), ('D', 0, -1), ('R', 1, 0), ('L', -1, 0)]
    ddict = {ll[0]:(ll[1], ll[2]) for ll in llist}
    cnt = 0
    visited = set()
    for ddir in dirs:
        nx = cur_x + ddict[ddir][0]
        ny = cur_y + ddict[ddir][1]
        if nx<-5 or nx>5 or ny<-5 or ny>5: continue
        if (nx, ny, ddir) in visited: 
            cur_x, cur_y = nx, ny
            continue
        cnt += 1
        if ddir == 'U':
            op_ddir = 'D'
        elif ddir == 'D':
            op_ddir = 'U'
        elif ddir == 'L':
            op_ddir = 'R'
        elif ddir == 'R':
            op_ddir = 'L'
            
        visited.add((nx, ny, ddir))
        visited.add((nx+ddict[op_ddir][0], ny+ddict[op_ddir][1], op_ddir))
        cur_x, cur_y = nx, ny

        
    return cnt