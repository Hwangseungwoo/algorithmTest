import math

def solution(progresses, speeds):
    answer = []
    # 최소 배포 기능 개수 정의
    feat = 1
    # 첫 번째 시간 설정
    time = math.ceil((100-progresses[0])/speeds[0])
    # 이전 프로세스들과 비교
    for i in range(1,len(progresses)):
        if time>=math.ceil((100-progresses[i])/speeds[i]):
            feat += 1
        else:
            answer.append(feat)
            feat = 1
            time = math.ceil((100-progresses[i])/speeds[i])
    answer.append(feat)
    
    return answer