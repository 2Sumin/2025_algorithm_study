def solution(array, commands):
    answer = []
    for tmp_list in commands:
        # 인덱스가 1부터 시작
        sliced_list = sorted(array[tmp_list[0]-1:tmp_list[1]])
        answer.append(sliced_list[tmp_list[2]-1])
    return answer
