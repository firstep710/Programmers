def solution(a, b):
    answer = ''
    day=0
    for i in range(1,a):
        if(i<8 and i%2==1):
            day+=31
        elif(i>7 and i%2==0):
            day+=31
        elif(i==2):
            day+=29
        else:
            day+=30
    day+=b
    week=day%7
    if(week==0):
        answer='THU'
    elif(week==1):
        answer='FRI'
    elif(week==2):
        answer='SAT'
    elif(week==3):
        answer='SUN'
    elif(week==4):
        answer='MON'
    elif(week==5):
        answer='TUE'
    else:
        answer='WED'
    return answer
