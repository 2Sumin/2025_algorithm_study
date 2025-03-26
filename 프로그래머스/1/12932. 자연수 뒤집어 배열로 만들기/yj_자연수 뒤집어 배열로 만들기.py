def solution(n):
    # answer = []
    
    # 일단 쪼개서 배열에 담고 
    # 마지막 리스트 인덱스를 count 한 다음 마지막 부터 출력
    lst = list(map(int, str(n)))
    
    return lst[::-1]
