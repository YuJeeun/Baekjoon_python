def solution(record):
    answer = []
    ddict = {}
    llist = []
    for i in range(len(record)):
        if len(record[i].split(' ')) == 3:
            ddict[record[i].split(' ')[1]] = record[i].split(' ')[2]
        llist.append(record[i].split(' ')[0])
    answer = chat(llist, record, ddict)
    return answer

'''
1. 채팅방 나간 후 새로운 닉네임으로 다시 들어가기
2. 채팅방에서 닉네임 변경하기

기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경됨
최종적으로 개설자가 보게 될 메시지 배열 return

1 <= record <= 100,000

무지님이 들어왔습니다.
프로도님이 들어왔습니다.
무지님이 나갔습니다.
프로도님이 들어왔습니다.
== 채팅방에서 바꾼 경우에는 출력 X ==
최종적으로 프로도프로도프로도프로도로 나와야함
record[i].split(' ')[0]만 저장해놨다가 마지막에 출력하기
어떻게? list에 Enter, Enter, Leave, Enter 저장해두기
만약 record[i].split(' ')[0]이 Enter인데 [1]이 바뀌었다-> ddict 바꿔주기
change는 바로 바꿔주기
'''

def chat(llist, record, ddict):
    result = []
    for i in range(len(llist)):
        if llist[i] == 'Enter':
            result.append(f"{ddict[record[i].split(' ')[1]]}님이 들어왔습니다.")
        elif llist[i] == 'Leave':
            result.append(f"{ddict[record[i].split(' ')[1]]}님이 나갔습니다.")
    return result
