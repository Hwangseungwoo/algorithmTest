def solution(numbers, target):
    n = len(numbers)
    answer = 0
    # 재귀 함수 선언
    def dfs(idx, result):
        # 만약 n번째 확인했을때 인덱스 위치라면
        if idx == n:
            # 만약 결과가 원하는 값이면
            if result == target:
                nonlocal answer
                answer += 1
            return
        # 아니면 + 혹은 - 해서 다시 탐색
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    # 0부터 시작
    dfs(0,0)
    return answer