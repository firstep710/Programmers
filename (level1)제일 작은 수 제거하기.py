def solution(arr):
    a=min(arr)
    answer=[x for x in arr if x!=a]or[-1]
    return answer