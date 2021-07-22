def solution(s):
    answer = True
    n1,n2=0,0
    for i in s:
        if i =='(':
            n1+=1
        elif i == ')':
            n2+=1
        if n2>n1:
            break
    if s[-1]==')' and n1==n2:
        print(s[-1])
        answer= True
    else:
        answer= False

    return answer