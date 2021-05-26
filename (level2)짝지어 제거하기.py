def solution(s):
    answer = 1
    a=[]
    for i in s:
        if a==[]:
            a.append(i)
        elif a[-1]==i:
            a.pop()
        else:
            a.append(i)
    if a:
        answer=0

    return answer