from collections import Counter
def solution(participant, completion):
    # 배열 -> 정렬
    participant.sort()
    # 해시테이블 만들기 (선수명:해당 이름의 선수 수)
    completion_dict = dict(Counter(completion))

    for i in participant:
        if i in completion_dict and completion_dict[i]>=1:
            completion_dict[i]-=1
        else:
            return i
