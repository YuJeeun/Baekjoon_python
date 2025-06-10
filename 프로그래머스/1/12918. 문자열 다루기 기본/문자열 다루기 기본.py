def solution(s):
    llen = len(s)
    if llen == 4 or llen == 6:
        if s.isnumeric(): return True
        else: return False
    
    return False
