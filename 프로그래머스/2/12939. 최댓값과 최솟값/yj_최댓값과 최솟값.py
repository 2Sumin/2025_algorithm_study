def solution(s):
    
    # 받은 문자열을 청킹(공백을 기준으로)
    # 문자 -> 숫자로 변형 (이때 리스트에 담기)
    # 리스트 내에서 최대와 최소 구하기
    # 출력 
    
    numbers = list(map(int, s.split()))
    
    min_num = min(numbers)
    max_num = max(numbers)
    
    return f"{min_num} {max_num}"
