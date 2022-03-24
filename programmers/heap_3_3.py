import heapq

# 배열 1개 풀이
def solution(operations):
    answer = []
    
    heap = []
    
    for i in range(len(operations)):
        com, num = operations[i].split(" ")
        if com=='I':
            heapq.heappush(heap, int(num))
        elif com=='D' and num=='1':
            if len(heap)!=0:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
        else:
            if len(heap)!=0:
                heapq.heappop(heap)
    if len(heap)==0:
        answer = [0,0]
        
    else:
        mx = max(heap)
        mn = min(heap)
        answer = [mx, mn]
    return answer