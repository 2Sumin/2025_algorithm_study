def solution(array, commands):
    answer = []
    
    for i ,j, k in commands:
        s =array[i-1:j]
        s.sort()
        answer.append(s[k-1])
    
    return answer
