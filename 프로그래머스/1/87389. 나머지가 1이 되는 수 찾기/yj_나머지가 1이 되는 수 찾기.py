1
2
3
4
5
6
7
8
def solution(n):
    x = 1

    while n % x != 1:
        x+=1

    return x
