def solution(jobs):
    answer = 0
    time=0
    b=-1
    i=0
    heap=[]
    while i<len(jobs):
        for j in jobs:
            if b < j[0] and j[0] <= time:
                heap.append(j)
        heap.sort(key=lambda x:x[1])
        if heap!=[]:
            b=time
            a=heap.pop(0)
            time+=a[1]
            answer+=time-a[0]
            i+=1
        else:
            time+=1
    return answer//len(jobs)