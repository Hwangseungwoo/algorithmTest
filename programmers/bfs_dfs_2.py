def solution(n, computers):
    answer1 = 0
    answer2 = 0
    visited1 = [False for i in range(n)]
    visited2 = [False for i in range(n)]
    for com in range(n):
        if visited1[com] == False:
            DFS(n, computers, com, visited1)
            answer1 += 1
    for com in range(n):
        if visited2[com] == False:
            BFS(n, computers, com, visited2)
            answer2 += 1
    return answer1

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: 
            if visited[connect] == False:
                DFS(n, computers, connect, visited)
                
                
def BFS(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)