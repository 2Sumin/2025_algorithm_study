def solution(x):
    sum_x = sum(int(i) for i in str(x))    # x의 자릿수 합
    return x % sum_x == 0