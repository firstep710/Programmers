def solution(phone_book):
    answer = True
    
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if(j!=i and phone_book[i] == phone_book[j][:len(phone_book[i])]):
                answer=False
        
    return answer