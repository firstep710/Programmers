def solution(participant, completion):
    completion.sort()
    participant.sort()
    while(completion):
        i=0
        while(participant):
            if(completion[0]==participant[i]):
                del completion[0]
                del participant[i]
                break
            else:
                i+=1
    return participant[0]
    