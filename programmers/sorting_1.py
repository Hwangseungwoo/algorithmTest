def solution(array, commands):
    
    # return 개수 확인
    length = len(commands)
    answer = []
    
    for i in range(length):
        start = commands[i][0]-1
        end = commands[i][1]
        new_list = []
        for k in range(start,end):
            new_list.append(array[k])
        new = new_list.sort()
        find = commands[i][2]-1
        answer.append(new_list[find])
        
    
    return answer