def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a=[]
        for j in range(commands[i][0]-1,commands[i][1]):
            a.append(array[j])
            a=sorted(a)
        answer.append(a[commands[i][2]-1])
    return answer
