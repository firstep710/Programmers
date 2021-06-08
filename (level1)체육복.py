def solution(n, lost, reserve):
    answer = 0
    std=[1]*n
    for j in range(len(reserve)):
        std[reserve[j]-1]+=1
    for i in range(len(lost)):
        std[lost[i]-1]-=1
    for k in range(0,n):
        if(std[k]==2):
            if(k==0):
                if(std[k+1]==0):
                    std[k+1]+=1
            elif(k==n-1):
                if(std[k-1]==0):
                    std[k-1]+=1
            elif(k>0 and k<n-1):
                if(std[k-1]==0):
                    std[k-1]+=1
                elif(std[k+1]==0):
                    std[k+1]+=1  
            std[k]-=1
    answer=sum(std)
    return answer
    