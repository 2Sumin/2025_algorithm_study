def solution(arr, divisor):
    
    result = [num for num in arr if num % divisor == 0]
    
    # 만약 나누어 떨어지는 값이 없다면 [-1] 반환
    return sorted(result) if result else [-1]
