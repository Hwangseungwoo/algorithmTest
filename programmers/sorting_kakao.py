def solution(N, stages):
    answer = [0]*N
    # 최초 sort
    stages.sort()
    num = len(stages)
    # stage 돌기
    for i in range(1,N+1):
        cnt = 0
        # 실패 목록 스테이지 중에 있으면 +1
        for j in range(len(stages)):
            if stages[j]==i:
                cnt += 1
        # 만약 해당 스테이지 도달 인원 != 0
        if num!=0:
            per = float(cnt/num)    # 실패/도달
            answer[i-1]= [per,i]    # 스테이지 sorting위해 같이 할당
            stages = stages[cnt:]   # 해당 스테이지에서 탈락 인원 제외
            num = len(stages)
        # 해당 스테이지 도달 인원 == 0
        else:
            answer[i-1] = [0,i]
        
    # 실패율은 내림차순, 스테이지는 오름차순
    new = sorted(answer, key=lambda x : (-x[0], x[1]))
    answer = []
    for i in new:
        answer.append(i[1])
    
    return answer