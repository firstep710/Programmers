def solution(numbers):
    answer = []
    for i in numbers:
        if i%2==0:
            a=list(bin(i)[2:])
            a[-1]='1'
        else:
            a='0'+bin(i)[2:]
            idx=a.rfind('0')
            a=list(a)
            a[idx]='1'
            a[idx+1]='0'
        answer.append(int(''.join(a),2))
    return answer