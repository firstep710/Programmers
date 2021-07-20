def solution(arr):
    answer = [0,0]
    l = len(arr)
    def quad(x, y, n):
        init = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init :
                    n_ = n // 2 
                    quad(x, y, n_)
                    quad(x + n_, y, n_)
                    quad(x, y + n_, n_)
                    quad(x + n_, y + n_, n_)
                    return
        answer[init] += 1
        return
    quad(0,0,l)
    return answer
