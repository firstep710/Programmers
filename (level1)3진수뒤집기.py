def solution(n):
    answer = 0
    a=[]
    while(n>0):
        a.append(n%3)
        n=int(n/3)
    a=a[::-1]
    for i in range(len(a)):
        answer+=a[i]*(3**i)
        print(answer)
    return answer
