def solution(brown, yellow):
    answer = []
    all = brown+yellow
    for i in range(1, int(yellow**0.5)+1):
        if yellow%i==0:
            second = i
            first = int(yellow/i)
            b_size = (first+2)*(second+2)
            if b_size == all:
                answer = [first+2, second+2]
        
    return answer