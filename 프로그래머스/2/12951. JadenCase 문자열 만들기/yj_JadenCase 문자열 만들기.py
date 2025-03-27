def solution(s):
     
    # 1
    # words = s.split(' ')  # 공백 기준으로 단어 분리
    # result = []
    
    # for word in words:
        # if word:  # 단어가 비어있지 않다면
            # result.append(word[0].upper() + word[1:].lower())  
        # else:  # 공백만 있는 경우 그대로 추가
            # result.append('')
    
    # return ' '.join(result)
    
    # 2
    return ' '.join(word.capitalize() for word in s.split(' '))
    # capitalize() : 문자열에서 첫 글자가 알파벳이면 대문자로 변환하고, 나머지는 소문자로 변환함.
    # 첫 글자가 숫자이면 그대로 둠.
