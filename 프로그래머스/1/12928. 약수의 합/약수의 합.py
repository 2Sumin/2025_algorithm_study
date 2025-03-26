def solution(n):
    if n==1:
        return 1
    # 중복되는 수 없도록 set 사용
    divisors = set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.add(i)
            divisors.add(n//i)
    return sum(divisors)