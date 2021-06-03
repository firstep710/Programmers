def solution(operations):
    answer = []
    for i in operations:
        a,b=i.split()
        b=int(b)
        if a=="I":
            answer.append(b)
        elif a=="D":
            if answer:
                if b==-1:
                    answer.remove(min(answer))
                else:
                    answer.remove(max(answer))
    if answer==[]:
        answer=[0,0]
    else:
        answer=[max(answer),min(answer)]
    return answer