def solution(numbers):
    answer = ''
    leng = len(numbers)
    
    # int to string
    for i in range(leng):
        num = numbers[i]
        numbers[i] = str(num)
        
    # 최대 3자리, sorting by 자릿수
    numbers = sorted(numbers, key=lambda x : x*3)
    
    # numbers에 없을때까지
    while leng!=0:
        mx = numbers[leng-1]
        answer = answer + str(mx)
        del numbers[leng-1]
        leng = len(numbers)

    # 만약 처음 시작이 '0'이면(0만 있을 경우, 예외처리)
    if answer[0]=='0':
        answer = '0'
    return answer