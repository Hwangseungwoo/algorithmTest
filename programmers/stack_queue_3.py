def solution(bridge_length, weight, truck_weights):
    # 시간, 끝난트럭수, 다리위트럭 정의
    time = 0
    move = []
    finish = 0
    cnt = len(truck_weights)
    
    # 끝난트럭이 전부가 아닐떄
    while finish<cnt:
        time += 1
        bridge_weight = 0
        # 만약 아무도 다리위에 없고 아직 남아있으면, [트럭무게, 간 거리(defualt 1)]
        if len(move)==0 and len(truck_weights)!=0:
            move.append([truck_weights.pop(0),1])
        else:
            # list out of index 예외처리 위한 list
            out_idx = []
            # 돌면서 움직인 거리 1 추가
            for i in range(len(move)):
                move[i][1] += 1
                # 만약 도착하면 해당 인덱스 저장
                if move[i][1]>bridge_length:
                    out_idx.append(i)
                    finish += 1
                # 아니라면 다리 위 무게에 추가
                else:
                    bridge_weight = move[i][0] + bridge_weight
            # 도착한 트럭 제거
            for i in range(len(out_idx)):
                del move[i]
            # 다리 위 무게 여유 있으면 다리 위에 트럭 추가
            if len(truck_weights)!=0 and (bridge_weight+truck_weights[0]<=weight):
                move.append([truck_weights.pop(0),1])
                    
    return time