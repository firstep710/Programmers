def solution(name):
    answer = 0
    a=ord('A')
    b=[]
    c=0
    idx=[]
    for i in range(1,len(name)//2):
        if ord(name[i])!=a:
            b.append(i)
    for i in range(len(name)//2,len(name)):
        if ord(name[i])!=a:
            idx.append(i)
    if b!=[]:
        if min(idx)-max(b)>len(name)//2:
            answer+=(max(b)*2+(len(name)-min(idx)))
        else:
            answer+=min(len(name)-min(b),max(idx))
    else:
        answer+=len(name)-min(idx)
    for i in list(name):
        if ord(i) != a:
            if ord(i)<=a+((ord("Z")-a+1)//2):
                answer+=ord(i)-a
            else:
                answer+=ord("Z")-ord(i)+1
    return answer

print(solution("AAABAAAAAB"))