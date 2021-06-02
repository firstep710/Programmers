def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0:
        answer+=5*len(cities)
    else:
        stack=[]
        for i in cities:
            if len(stack)<cacheSize:
                if i.lower() in stack:
                    answer+=1
                    del stack[stack.index(i.lower())]
                    stack.append(i.lower())
                else:
                    stack.append(i.lower())
                    answer+=5
            else:
                if i.lower() in stack:
                    answer+=1
                    del stack[stack.index(i.lower())]
                    stack.append(i.lower())
                else:
                    answer+=5
                    stack.pop(0)
                    stack.append(i.lower())
    return answer