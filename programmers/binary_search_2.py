def solution(distance, rocks, n):
    answer = 0
    mid = distance//2
    rocks.sort()
    for i in range(len(rocks)):
        for j in range(i+1, len(rocks)):
            new_rocks = rocks[:]
            first = new_rocks[i]
            second = new_rocks[j]
            new_rocks.remove(first)
            new_rocks.remove(second)
            dis = []
            for k in range(len(new_rocks)+1):
                if k==0:
                    dis.append(new_rocks[k])
                elif k==len(new_rocks):
                    dis.append(distance-new_rocks[len(new_rocks)-1])
                else:
                    dis.append(new_rocks[k]-new_rocks[k-1])
            mini = min(dis)
            if mini>answer:
                answer = mini
                
    return answer