import heapq

def solution(scoville, K):
    answer = 0
    # 리스트 to 최소힙
    heapq.heapify(scoville)
    # 루프 돌기 위한 조건
    finish = False
    
    while finish==False: 
        # 만약 최소값이 K보다 크면 return
        if scoville[0]>=K:
            return answer
        # 만약 최소값이 K보다 크지 않은데 힙에 1개 요소만 있으면 break
        if len(scoville)==1:
            finish == True
            break
        # 최소값 1,2 pop
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        # 계산 후 push
        new = min_1 + min_2*2
        heapq.heappush(scoville, new)
        answer += 1
        
    return -1