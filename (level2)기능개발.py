import math

def solution(progresses, speeds):
    answer = []
    service = 1
    left = []
    
    for i in range(len(progresses)):
        left.append(math.ceil((100-progresses[i])/speeds[i]))
    while(len(left)>0):
        a=left.pop(0)
        for i in range(len(left)):
            if(a>=left[0]):
                del left[0]
                service +=1
            else:
                break
        answer.append(service)
        service = 1
        
    return answer