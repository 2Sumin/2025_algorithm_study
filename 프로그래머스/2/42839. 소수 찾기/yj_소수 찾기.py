from itertools import permutations
import math

# 소수 판별 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    
    # split 해서 int화 
    nums = list(numbers) # 문자열을 리스트로 쪼개기
    candidates = set() # 중복제거 / 011 과 11은 같음 
    
    # 모든 숫자 조합해 보기 
    for i in range(1, len(nums)+1): # 1자리 숫자 부터 만들수 있는 가장 긴 자리 숫자까지 
        for p in permutations(nums, i):
            num = int("".join(p))
            candidates.add(num)
            
    answer = 0
    for x in candidates: 
        if is_prime(x):
            answer+=1
    
    return answer
