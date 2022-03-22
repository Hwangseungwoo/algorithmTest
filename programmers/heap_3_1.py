import heapq

# heap 사용한 풀이
def solution(operations):
    answer = []
    
    min_heap = []
    max_heap = []
    cnt = 0
    for i in range(len(operations)):
        com, num = operations[i].split(" ")
        # I이면 min heap, max heap에 push
        if com=='I':
            # 없으면 heap 초기화
            if cnt == 0:
                min_heap = []
                max_heap = []
                heapq.heappush(min_heap, int(num))
                heapq.heappush(max_heap, (-int(num), int(num)))
            else:
                heapq.heappush(min_heap, int(num))
                heapq.heappush(max_heap, (-int(num), int(num)))
            cnt = cnt +1 
        # D이고 1이면 max heap에서 최소 pop
        elif com=='D' and num=='1':
            if cnt!=0:
                heapq.heappop(max_heap)
                cnt = cnt -1
        # D이고 -1이면 최소 pop
        else:
            if cnt!=0:
                heapq.heappop(min_heap)
                cnt = cnt -1
    
    # heap에 없으면
    if cnt==0:
        answer = [0,0]
    # 아니면 최소, 최대
    else:
        answer.append(heapq.heappop(max_heap)[1])
        answer.append(heapq.heappop(min_heap))
    return answer