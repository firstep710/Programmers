def solution(prices):
    answer = [0]*len(prices)
    
    for j in range(len(prices)):
        for i in range(j+1,len(prices)):
            answer[j] +=1
            if(prices[j]>prices[i]):
                break

    return answer