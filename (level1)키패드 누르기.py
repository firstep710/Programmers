def solution(numbers, hand):
    key_pad=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    l=[3,0]
    r=[3,2]
    answer = ''
    while numbers:
        a=numbers.pop(0)
        for i in range(len(key_pad)):
            for j in range(3):
                if a==key_pad[i][j]:
                    if a==1 or a==4 or a==7:
                        answer+='L'
                        l=[i,j]
                    elif a==3 or a==6 or a==9:
                        answer+='R'
                        r=[i,j]                    
                    else:
                        l_d=abs(i-l[0])+abs(j-l[1])
                        r_d=abs(i-r[0])+abs(j-r[1])
                        if l_d>r_d:
                            answer+='R'
                            r=[i,j]
                        elif l_d<r_d:
                            answer+='L'
                            l=[i,j]
                        elif l_d==r_d:
                            answer+=hand[0].upper()
                            if hand=='left':
                                l=[i,j]
                            else:
                                r=[i,j]
                    
                                
                    
    return answer