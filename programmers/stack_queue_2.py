def solution(priorities, location):
    new_prior = []
     # new_prior = [(idx,p) for idx,p in enumerate(priorities)] enumerate도 존재
    for i in range(len(priorities)):
        new_prior.append((i, priorities[i]))  
    # 우선순위 최초 설정
    prior = 0
    # FIFO, queue 사용
    while len(new_prior)!=0:
        cur = new_prior.pop(0)
        # queue value 값 중 하나라도 우선순위가 현재값보다 큰지 비교
        if any(cur[1]<p[1] for p in new_prior):
            new_prior.append(cur)
        else:
            if cur[0]==location:
                prior += 1
                answer = prior
            else:
                prior += 1
    return answer