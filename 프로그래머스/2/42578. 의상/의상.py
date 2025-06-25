def solution(clothes):
    ans = 1
    # 딕셔너리에 넣기
    dict_clo = {}
    for set in clothes:
        if set[1] not in dict_clo:
            dict_clo[set[1]] = 1    
        else:
            dict_clo[set[1]] += 1
    # 각 종류별로 입는 경우/안 입는 경우 존재
    # 각 종류마다 (해당 종류의 옷 개수 + 1) 가지 선택 가능 (1: 안 입는 거)
    for cnt in dict_clo.values():
        ans *= (cnt+1)
    # 아무것도 안 입는 경우 뺌
    return ans-1