def solution(phone_book):
    # 딕셔너리에 번호 저장
    dict_num = {}
    for i in phone_book:
        dict_num[i]=True
    # 현재 번호의 앞부분을 번호로 가지는 (접두어)가 존재하고, 자기 자신이 아니라면 리턴
    for num in phone_book:
        prefix=''
        for i in num:
            prefix+=i
            if prefix in dict_num and prefix!=num:
                return False
    return True
