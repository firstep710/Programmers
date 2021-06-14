def solution(people, limit):
    answer = len(people)
    people.sort()
    a=0
    b=len(people)-1
    while(a<b):
        if(people[a]+people[b]<=limit):
            a+=1
            b-=1
            answer-=1
        elif(people[a]+people[b]>limit):
            b-=1
    return answer