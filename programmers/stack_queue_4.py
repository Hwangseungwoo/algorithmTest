def solution(prices):
    # 배열 0으로 다 초기화
    answer = [0] * len(prices)
    
    # loop 2개
    for i in range(len(prices)):
        # i 인덱스 이후 리스트 확인
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
