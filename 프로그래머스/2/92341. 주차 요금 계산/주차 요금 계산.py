import math

def solution(fees, records):
    answer = []
    result = []
    result = append_record(fees, records)
    for i in range(len(result)):
        answer.append(result[i][1])
    return answer

def append_record(fees, records):
    ddict = {}
    result = {}
    for i in range(len(records)):
        h = int(records[i].split(' ')[0].split(':')[0])
        m = int(records[i].split(' ')[0].split(':')[1])
        time = h*60 + m
        
        # dict에 없고 입차면 시간 기록
        if records[i].split(' ')[1] not in ddict and records[i].split(' ')[2] == 'IN': 
            result[records[i].split(' ')[1]] = 0
            ddict[records[i].split(' ')[1]] = [time, True]
            
        elif records[i].split(' ')[2] == 'IN': 
            ddict[records[i].split(' ')[1]] = [time, True]

        # 출차면 시간 result에 기록, ddict는 0
        else:
            result[records[i].split(' ')[1]] += abs(ddict[records[i].split(' ')[1]][0] - time)
            ddict[records[i].split(' ')[1]] = [0, False]
        
    for key, values in ddict.items():
        if values[1]:
            result[key] += abs(values[0] - 1439)
            
        if result[key] <= fees[0]:
            result[key] = fees[1]
            continue
        
        result[key] = fees[1] + math.ceil(abs(result[key]-fees[0])/fees[2])*fees[3]
    result = sorted(result.items())
    return result