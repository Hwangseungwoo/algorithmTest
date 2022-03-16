def solution(genres, plays):
    answer = []
    
    # 전체 장르 plays 합산 순서 확인
    dic = {}
    for i in range(len(genres)):
        type = genres[i]
        if type in dic:
            dic[type] += plays[i]
        else:
            dic[type] = plays[i]
    dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
    
    # 장르 순서 확인
    lst = []
    for i in range(len(dic)):
        lst.append(dic[i][0])
    
    # (인덱스, 장르, 플레이수) 저장 후 플레이수 기준 정렬
    new_dic = []
    for i in range(len(genres)):
        new_dic.append((i, genres[i], plays[i]))
    new_dic.sort(key=lambda x : x[2],reverse=True)
    
    # 최다 장르 순서대로 2개씩 추출
    for i in lst:
        cnt = 0
        for j in range(len(new_dic)):
            if new_dic[j][1] == i:
                answer.append(new_dic[j][0])
                cnt += 1
                if cnt == 2:
                    break
        
    return answer