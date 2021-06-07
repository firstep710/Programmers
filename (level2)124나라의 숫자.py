def solution(n):
    answer = ''
    a=[]
    while(n>3):
        a.append((n-1)%3)
        n=int((n-1)/3)
    a.append(n-1)
    a=a[::-1]
    for i in range(len(a)):
        if(a[i]==0):
            answer+='1'
        elif(a[i]==1):
            answer+='2'
        elif(a[i]==2):
            answer+='4'
    return answer
    