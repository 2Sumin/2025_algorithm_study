def solution(nums):
    needed_cnt = len(nums)/2
    cnt = 0 
    nums_dict={}
    # nums 리스트 순회하면서 딕셔너리에 없는 종류이면 추가
    for i in nums:
        if i not in nums_dict:
            nums_dict[i]=1
            cnt+=1
            if needed_cnt == cnt:
                return cnt
    # 중복이 필요한 경우는 현재 가짓수가 최대이므로 그대로 리턴
    return cnt
