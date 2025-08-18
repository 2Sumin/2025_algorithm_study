def solution(answers):
    res = [0,0,0]
    
    # 수포자 찍기 패턴
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 맞추면 카운팅 +1 
    for i, ans in enumerate(answers): 
        if ans == p1[i%len(p1)]:
            res[0] += 1
        if ans == p2[i%len(p2)]:
            res[1] += 1
        if ans == p3[i%len(p3)]:
            res[2] += 1
    
    
    max_score = max(res)
    
    result = []
    for i in range(len(res)):
        if res[i] == max_score:
            result.append(i+1)
    
    return result
