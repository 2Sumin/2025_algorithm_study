def solution(phone_book):
    
    # 어떤 번호가 다른 번호의 접두어인 경우가 있으면
    # -> false 
    # 없으면 
    # -> true
    
    # [로직]
    # 전화번호들을 모두 해시에 넣기 
    # 배열에서 짧은 순대로 시도하기 (사전순 배열) -> 바로 옆의 문자열과 비교가능함.
      
    phone_set = set(phone_book)
    phone_book.sort()

    for i in range(len(phone_book) - 1):
            # 앞 번호가 다음 번호의 접두어인지 확인
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
    
   # 처음엔 길이순으로 정렬 후 첫번째 문자열을 뒤의 것들과 비교하려 했는데 예: sort(key=len(phone_book))
   # 사전식 정렬이 훨씩 효율적
