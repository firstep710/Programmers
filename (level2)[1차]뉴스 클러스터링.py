import re
def solution(str1, str2):
    answer = 0
    l1=[]
    l2=[]
    count=0
    b=0
    c=0
    for i in range(len(str1)-1):
        a=re.findall('[a-z]+',str1[i:i+2].lower())
        if len(a)>0 and len(a[0])==2:
            l1.append(a[0])
    for i in range(len(str2)-1):
        a=re.findall('[a-z]+',str2[i:i+2].lower())
        if len(a)>0 and len(a[0])==2:
            l2.append(a[0]) 
    if l1:
        c=len(l1)+len(l2)
        for i in l1:
            if i in l2:
                count+=1
                l2.remove(i)
        b=c-count
        answer=int(count/b*65536)
    elif l1==[] and l2==[]:
        answer=65536
    return answer