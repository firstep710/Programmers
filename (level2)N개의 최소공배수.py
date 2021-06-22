def solution(arr):
    a=1
    answer = 0
    while 1:
        m=True
        num=arr[-1]*a
        for i in arr:
            if num%i != 0:
                m=False
            if m==False:
                break
        if m==True:
            answer=num
            break
        else:
            a+=1
    
    return answer