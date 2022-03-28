def solution(citations):
    answer = 0
    lst = []
    
    # sorting
    citations.sort()
    leng = len(citations)
    
    # loop
    for i in range(leng):
        # 해당 값 이상 논문 수
        cnt = leng - i
        # 만약 해당 값이 논문 수보다 크면
        if citations[i]>=cnt:
            lst.append(cnt)
    
    # 빈 배열이면 0
    if len(lst)==0:
        answer = 0
    else:
        answer = max(lst)
    return answer