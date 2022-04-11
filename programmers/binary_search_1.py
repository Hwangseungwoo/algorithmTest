def solution(n, times):
    answer = 0
    
    # 이분 탐색 할 최대 최소 값 설정(시간)
    left, right = 1, max(times) * n
    
    # loop 조건
    while left <= right:
        mid = (left+ right) // 2
        people = 0
        
        # 최대 심사 가능 사람 확인
        for time in times:
            people += mid // time
            
            # 최대 심사가 input보다 크면 그만(time complexity)
            if people >= n:
                break
        # 중간값보다 더 가능하면 오른쪽 이분탐색
        if people >= n:
            answer = mid
            right = mid - 1
        # 중간값이 불가능하면 왼쪽 이분탐색
        elif people < n:
            left = mid + 1
            
    return answer