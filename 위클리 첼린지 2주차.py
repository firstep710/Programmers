def solution(scores):
    answer = ''
    a=len(scores)
    for i in range(a):
        score=[]
        for j in range(a):
            score.append(scores[j][i])
        if min(score) == score[i] or max(score) == score[i]:
            if score.count(score[i])==1:
                score.pop(i)
                print(score)
        avr=float(sum(score)/len(score))
        if avr>=90:
            answer+='A'
        elif avr>=80:
            answer+='B'
        elif avr>=70:
            answer+='C'
        elif avr>=50:
            answer+='D'
        else:
            answer+='F'    
    return answer