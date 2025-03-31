def solution(phone_book):
    answer = find_prefix(phone_book)
    return answer 

def find_prefix(phone_book):
    phone_book.sort()
    # 정렬을 하고 나면 바로 다음 번호만 비교해보면 됨.
    # 만약 접두사라면 다음거는 확인할 필요 없이 false 반환
    # 접두사가 아니라면 그 다음것도 아닌거니까 true 반환
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
                
                    