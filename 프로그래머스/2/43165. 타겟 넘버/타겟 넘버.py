def solution(numbers, target):
    cnt = 0

    def dfs(cur_idx, cur_sum): # 다음에 더할 값의 인덱스와 현재까지의 합
        nonlocal cnt
        # cur_idx가 배열의 길이라면 cur_sum에는 cur_idx-1까지의 합이 저장
        # -> 리스트 내 모든 원소의 합 저장
        if cur_idx == len(numbers):
            if cur_sum == target:
                cnt+=1
            return
        # 다음 재귀함수 실행 시 사용할 인덱스, 현재까지의 합 전달
        dfs(cur_idx + 1, cur_sum + numbers[cur_idx])
        dfs(cur_idx + 1, cur_sum - numbers[cur_idx])
        
    dfs(0,0)
    return cnt