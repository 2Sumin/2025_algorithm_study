def solution(numbers):
    str_numbers = [str(num) for num in numbers]
    # 두 숫자를 이어붙일 때 어느 순서가 더 큰 수를 만드는지 판단해야함
    # -> 단순히 sort()하지 않고 각 숫자를 이어붙였을 때의 숫자를 기준으로 정렬
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    
    if str_numbers[0] == '0':
        return '0'
    
    return ''.join(str_numbers)
