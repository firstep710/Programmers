def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        a=[]
        correct=True
        for j in i:
            if j in skill:
                a.append(j)
        for k in range(len(a)):
            if a[k]!=skill[k]:
                correct=False
                break
        if correct==True:
            answer+=1
        
    return answer