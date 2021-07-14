def rotate(y1,x1,y2,x2,arr):
    mini=arr[x1][y1]
    temp=arr[x1][y1]
    for i in range(x1,x2):
        test=arr[i+1][y1]
        arr[i][y1]=arr[i+1][y1]
        mini=min(test,mini)
    for i in range(y1,y2):
        test=arr[x2][i+1]
        arr[x2][i]=arr[x2][i+1]
        mini=min(test,mini)
    for i in range(x2,x1,-1):
        test=arr[i-1][y2]
        arr[i][y2]=arr[i-1][y2]
        mini=min(test,mini)
    for i in range(y2,y1,-1):
        test=arr[x1][i-1]
        arr[x1][i]=arr[x1][i-1]
        mini=min(test,mini)
    arr[x1][y1+1]=temp
    return mini
def solution(rows, columns, queries):
    answer = []
    form = []
    num = 1;
    for i in range(rows):
        now = []
        for j in range(columns):
            now.append(num);
            num += 1;
        form.append(now);
    for i in queries:
        answer.append(rotate(i[1]-1,i[0]-1,i[3]-1,i[2]-1,form))
    return answer