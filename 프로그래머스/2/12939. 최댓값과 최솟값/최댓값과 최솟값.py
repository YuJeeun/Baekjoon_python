def solution(s):
    sstr = list(map(int, s.split(' ')))
    mmax, mmin = str(max(sstr)), str(min(sstr))
    return mmin + ' ' + mmax