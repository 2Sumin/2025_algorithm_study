def solution(numbers):
    # 차집합으로 없는 숫자 구하기
    # range(10): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - range 객체
    # set(range(10)): {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    missing_numbers = set(range(10)) - set(numbers)
    return sum(missing_numbers)
