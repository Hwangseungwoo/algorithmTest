import heapq

def solution(jobs):
    # 총 대기시간, 현재 시간 및 길이 정의
    answer = 0
    time = 0
    cnt = len(jobs)
    num = len(jobs)

    # min heap위해 [소요시간,요청시각]으로 변경
    for i in range(num):
        start = jobs[i][0]
        takes = jobs[i][1]
        jobs[i][0] = takes
        jobs[i][1]=start

    # min heap 만든 이후 소요시간 최소값부터 pop하여 list 정렬
    heapq.heapify(jobs)
    result = []
    for i in range(num):
        result.append(heapq.heappop(jobs))
    
    # 아직 작업이 있을경우에
    while num>0:
        # 꺼내올 작업 index
        idx = 0
        cur = 0
        find = False
        # 만약 현재시각보다 요청시각이 더 전인 값들 꺼내서 삭제
        for i in range(num):
            if time>=result[i][1]:
                idx = i
                cur = result[i]
                find = True
                del result[idx]
                break
        # 만약 현재시각보다 요청시각이 전인 값이 있을경우
        if find==True:
            # 대기시간 = 현재시각-요청시각+걸린시간
            answer = answer + time - cur[1]+cur[0]
            # 현재시각에 소요시간 추가
            time = time + cur[0]
            # 제거된 list 길이 다시 측정
            num = len(result)
        # 만약 현재시각보다 요청시각이 전인 값이 없을 경우 현재시각 +1
        else:
            time += 1
            
    # 평균대기시간
    return int(answer/cnt)