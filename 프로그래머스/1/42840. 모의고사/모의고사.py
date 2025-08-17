def solution(answers):
    # 각 수포자의 찍기 패턴
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자의 정답 개수
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for idx, ans in enumerate(answers):
        # 패턴은 반복되므로 나머지 연산 사용
        if pattern1[idx % len(pattern1)] == ans:
            cnt1 += 1
        if pattern2[idx % len(pattern2)] == ans:
            cnt2 += 1
        if pattern3[idx % len(pattern3)] == ans:
            cnt3 += 1
    
    # 최고 점수 
    max_score = max(cnt1, cnt2, cnt3)
    
    # 최고 점수를 받은 사람들 찾기
    result = []
    if cnt1 == max_score:
        result.append(1)
    if cnt2 == max_score:
        result.append(2)
    if cnt3 == max_score:
        result.append(3)
    
    return result