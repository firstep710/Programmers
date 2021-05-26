def solution(lottos, win_nums):
    answer = []
    win_nums=set(win_nums)
    a=[]
    correct=0
    for i in lottos:
        if i in win_nums:
            a.append(i)
        elif i==0:
            correct+=1
    correct+=len(a)
    rank={0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    answer.append(rank[correct])
    answer.append(rank[len(a)])
    return answer
