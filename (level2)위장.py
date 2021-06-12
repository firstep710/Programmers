from collections import Counter

def solution(clothes):
    answer = 0
    wear=[]
    for i in clothes:
        wear.append(i[1])
    c=Counter(wear)
    if(len(wear)==1):
        answer=list(c.values())[0]
    else:
        b=1
        for i in list(c.values()):
            b*=(i+1)
        answer=b-1
        
    return answer