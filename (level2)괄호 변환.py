def iscorrect(u):
    count=0
    for i in u:
        if i=="(":
            count+=1
        elif i==")":
            count-=1
        if count<0:
            return False
    return True

def divide(p):
    c=0
    for i in range(len(p)):
        if p[i]=="(":
            c+=1
        else:
            c-=1
        if c==0:
            return p[:i+1],p[i+1:]
    
def solution(p):
    if p=="":
        return ""
    answer = ''
    u,v=divide(p)
    if iscorrect(u):
        return u+solution(v)
    
    if iscorrect(u):
        answer+=u
    else:
        answer+="("
        answer+=solution(v)
        answer+=")"
        
        for i in range(1,len(u)-1):
            if u[i]=="(":
                answer+=")"
            else:
                answer+="("
    
    return answer