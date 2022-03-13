def solution(clothes):
    answer = 1
    # 딕셔너리, 리스트 생성
    dict = {}
    lst = []
    
    # 값 할당
    for i in clothes:
        type = i[1]
        if type in dict:
            dict[type] += 1
        else:
            dict[type] = 1
            lst.append(type)
            
    # 존재하는 타입 개수 확인 후 결과 도출
    for i in lst:
        answer = answer*(dict[i]+1)
    answer -= 1
    
    return answer