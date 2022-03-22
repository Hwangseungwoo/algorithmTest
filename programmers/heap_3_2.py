import heapq

# sort 사용한 풀이
def solution(operations):
    answer = []
    
    heap = []
    for i in range(len(operations)):
        com, num = operations[i].split(" ")
        if com=='I':
            heap.append(int(num))
        elif com=='D' and num=='1':
            if len(heap)!=0:
                mx = max(heap)
                mx_idx = heap.index(mx)
                del heap[mx_idx]
        else:
            if len(heap)!=0:
                mx = min(heap)
                mx_idx = heap.index(mx)
                del heap[mx_idx]
    if len(heap)==0:
        answer = [0,0]
    else:
        mx = max(heap)
        mn = min(heap)
        answer = [mx, mn]
    return answer