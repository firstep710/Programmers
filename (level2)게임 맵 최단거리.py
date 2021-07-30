def solution(maps):
    move=[[1,0],[-1,0],[0,1],[0,-1]]
    queue=[]
    ly=len(maps)
    lx=len(maps[0])
    a=[[-1 for _ in range(lx)]for _ in range(ly)]
    queue.append([0,0])
    a[0][0]=1
    while queue:
        y,x=queue.pop(0)
        for i in move:
            mx,my=i
            nx=x+mx
            ny=y+my
            if 0<=nx<lx and 0<=ny<ly and maps[ny][nx]==1:
                if a[ny][nx]==-1:
                    a[ny][nx]=a[y][x]+1
                    queue.append([ny,nx])
    answer = a[-1][-1]
    return answer