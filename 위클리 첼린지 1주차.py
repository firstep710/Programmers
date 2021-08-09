def solution(price, money, count):
    answer = -1
    a=0
    for i in range(count):
        a+=(price*(i+1))
    
    answer=a-money
    if a<=money:
        answer=0
    return answer