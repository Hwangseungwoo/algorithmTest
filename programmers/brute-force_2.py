from itertools import permutations

def solution(numbers):
    answer = 0
    prime = []
    check = []
    num = []
    per = []
    # 각 number 1개씩
    for i in range(len(numbers)):
        num.append(numbers[i])
    # 순열 조합 찾기
    for j in range(1, len(num)+1):
        per += list(permutations(num, j))
        
    # string list to int
    new_num = [int(("").join(p)) for p in per]
    
    # integer 내부에서
    for k in new_num:
        # 2 미만은 소수 x
        if k<2:
            continue
        # 이미 체크한 숫자인지 판별
        if k not in check:
            check.append(k)
            isPrime = True
            # 제곱근보다 작은 숫자까지만 나눠서 판별 -> 소수 판별
            for p in range(2, int(k**0.5)+1):
                if k%p==0:
                    isPrime = False
                    break
            if isPrime==True:
                    answer += 1                    

    return answer                     