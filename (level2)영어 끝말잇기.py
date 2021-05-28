def solution(n, words):
    answer = []
    stack=[]
    a=0
    for i in range(len(words)-1):
        stack.append(words[i])
        if words[i+1] in stack:
            a=i+1
            break
        elif words[i+1][0]!=stack[-1][-1]:
            a=i+1
            break
    else:
        answer.append(a)
        answer.append(a)
    if len(answer)==0:    
        answer.append((a%n)+1)
        answer.append((a//n)+1)
    return answer