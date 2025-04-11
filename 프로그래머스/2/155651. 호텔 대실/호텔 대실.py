def solution(book_time):
    sort_booktime(book_time)
    ddict = {}
    cnt = 1
    ddict[cnt] = book_time[0][1] 
    st = False

    for i in range(1, len(book_time)):
        ddict_len = len(ddict)
        st = False
        for j in range(1, ddict_len+1):
            if ddict[j]+10 <= book_time[i][0]:
                ddict[j] = book_time[i][1]
                st = True
                break
                
        if not st:
            cnt += 1
            ddict[cnt] = book_time[i][1]
        
    return len(ddict)

def sort_booktime(book_time):
    st = book_time[0][0]
    sh = st.split(':')[0]
    sm = st.split(':')[1]
    
    for time in book_time:
        st, et = time[0], time[1]
        sh, sm = int(st.split(':')[0])*60, int(st.split(':')[1])
        eh, em = int(et.split(':')[0])*60, int(et.split(':')[1])
        time[0], time[1] = sh+sm, eh+em
        
    book_time.sort(key=lambda x: x[0])