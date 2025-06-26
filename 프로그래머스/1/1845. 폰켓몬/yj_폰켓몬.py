def solution(nums):
    answer = 0
    
    # 배열을 돌면서 해시 맵으로 각 숫자별 개수를 카운트 해서 넣음 
    # N/2 이 해시 맵의 크기 (다른 수의 개수)보다 작으면 N/2 반환 
    # N/2 이 해시 맵의 크기보다 크면 다른 수의 크기를 반환

    # set() = 해시셋
    # dict() = 해시맵
    
    n = len(nums)
    kinds = len(set(nums))  # 중복 제거해서 고유한 종류 수 구함
    return min(kinds, n // 2)
