def solution(phone_book):
    # 정렬, 사전순
    phone_book=sorted(phone_book) 
    
    # 마지막 애는 비교할 거 없으므로 제거
    for i in range(len(phone_book)-1): 
        cur = phone_book[i]
        # 다음꺼랑만 비교, 사전순이므로
        if(cur==phone_book[i+1][:len(cur)]):
             return False

    return True