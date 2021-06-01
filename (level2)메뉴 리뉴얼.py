from itertools import combinations

def solution(orders, course):
    answer = []
    menu=sorted(list(set(''.join(orders))))
    orders=sorted(orders,key=lambda x:len(x), reverse=True)
    a=[]
    dic={}
    stack=[]
    for i in course:
        if i>len(orders[0]):
            break
        a=set(combinations(menu,i))
        b=[]
        for j in a:
            c=0
            for k in orders:
                if set(j).intersection(k)==set(j):
                    c+=1
            if c>1: 
                dic[j]=c
                b.append(c)
        if b!=[]:
            stack.append(max(b))
            q=stack.pop(0)
        for p in dic:
            if len(p)==i:
                if dic[p]==q:
                    answer.append(''.join(list(p)))
    
    return sorted(answer)