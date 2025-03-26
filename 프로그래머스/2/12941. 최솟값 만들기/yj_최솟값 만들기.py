def solution(A,B):

    # 한쪽 배열의 가장 큰 원소는 무조건 다른쪽 배열의 가방 작은 원소와 곱해져야 함. 
    # 배열들을 크기 순으로 오름차순 정렬. 
    # 그 다음 B[n-1] * A[0] + B[n-2] * A[1] + ...+ B[0] * A[n-1] => 값을 리턴하기
    
    A.sort()  # A를 오름차순 정렬
    B.sort(reverse=True)  # B를 내림차순 정렬
    
    result = 0
    
    for i in range(len(A)):  # A와 B의 길이는 같다고 가정
        result += A[i] * B[i]

    return result
