def solution(citations):
    answer = 0
    for i in range(0,max(citations)):
        index=[]
        for j in citations:
            if(j>=i):
                index.append(j)
        if(len(index)>=i):
            answer=i
    return answer
