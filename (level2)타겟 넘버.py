answer = 0
def solution(numbers, target):
    l=len(numbers)
    global answer
    def dfs(idx,n):
        if idx==l:
            if n==target:
                global answer
                answer+=1
            return 
        else:
            dfs(idx+1,n+numbers[idx])
            dfs(idx+1,n-numbers[idx])
    dfs(0,0)
    return answer