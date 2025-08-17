from itertools import permutations

def solution(numbers):
    # 소수 판별 함수
    def is_prime(n):
        if n < 2:  # 2보다 작은 수는 소수가 아님
            return False
        if n == 2:  # 2는 소수
            return True
        if n % 2 == 0:  # 짝수는 소수가 아님 (2 제외)
            return False
        
        # 3~root(n) 까지의 홀수로만 나누어 확인
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    # 만들 수 있는 모든 숫자들을 저장
    possible_numbers = set()
    
    # 1자리부터 numbers 길이까지 모든 길이의 순열 생성
    for length in range(1, len(numbers) + 1):
        # length개의 숫자를 선택하는 모든 순열
        for perm in permutations(numbers, length):
            # 순열을 문자열로 합치기
            num_str = ''.join(perm)
            
            # 맨 앞이 0이 아닌 경우만 유효한 숫자로 취급
            if num_str[0] != '0':
                possible_numbers.add(int(num_str))
    
    # 생성된 모든 숫자 중에서 소수인 것들의 개수 세기
    prime_count = 0
    for num in possible_numbers:
        if is_prime(num):
            prime_count += 1
    
    return prime_count
