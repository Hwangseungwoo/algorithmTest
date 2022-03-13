import math

def solution(participant, completion):
    # 딕셔너리 생성
    dict = {}
    
    # 참가자 확인
    for i in participant:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] =1
            
    # 완료자 확인
    for i in completion:
        if dict[i]==1:
            del dict[i]
        else:
            dict[i]-=1
    
    # 남아있는 딕셔너리 키 반환
    answer = list(dict.keys())[0]
    
    return answer