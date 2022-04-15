def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left = 1
    right = distance
    
    
    while left<=right:
        mid = (left+right) // 2
        cur = 0
        cnt = 0
        
        for i in range(len(rocks)):
            # 만약 거리가 더 길거나 같으면 내가 설정한 최소값에 문제 없으므로 그 다리 유지하고 다음과의 거리 체크
            if rocks[i]-cur>=mid:
                cur = rocks[i]
            # 만약 거리가 더 작으면 내가 설정한 최소값이랑 다르니까 없애는 목록 +1
            else:
                cnt += 1
        # 최종목적지랑 마지막돌이랑 거리도 확인
        if distance-cur<mid:
            cnt += 1
        
        # 만약 돌 없앤게 더 많으면 내가 설정한 최소값이 너무 큰거니까 왼쪽 이분 탐색
        if cnt>n:
            right = mid -1
        # 만약 돌 없앤거랑 같거나 작으면 최소값이 너무 작으니까 오른쪽 이분 탐색
        else:
            answer = mid
            left = mid +1
    
                
    return answer