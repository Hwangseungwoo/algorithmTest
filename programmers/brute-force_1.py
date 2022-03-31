def solution(answers):
    answer = []
    cnt1 = 0
    ans1 = [1,2,3,4,5]
    cnt2 = 0
    ans2 = [2,1,2,3,2,4,2,5]
    cnt3 = 0
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if ans1[i%5]==answers[i]:
            cnt1 += 1
        if ans2[i%8]==answers[i]:
            cnt2 += 1
        if ans3[i%10] == answers[i]:
            cnt3 += 1
    al = []
    al.append(cnt1)
    al.append(cnt2)
    al.append(cnt3)
    mx = max(al)
    for j in range(len(al)):
        if al[j]==mx:
            answer.append(j+1)
    
        
    return answer