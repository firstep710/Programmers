import re
def solution(new_id):
    ni=new_id.lower()
    a=re.compile('[a-z0-9-_.]')
    ni=''.join(a.findall(ni))
    c=ni.count('..')
    while c:
        c=ni.count('..')
        if '..' in ni:
            ni=ni.replace('..','.')
        else:
            break
    ni=list(ni)
    
    if ni[0]=='.':
        del ni[0]
    if ni=='':
        pass
    else:
        if ni[-1]=='.':
            del ni[-1]
    if len(ni)==0:
        ni.append('a')
    if len(ni)>=16:
        ni=ni[:15]
        if ni[-1]=='.':
            del ni[-1]
    while len(ni)<=2:
        ni.append(ni[-1])
    print(ni)
    answer = ''.join(ni) 
    return answer
