def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    
    for i in range(len(citations)):
        papers_count = i + 1  # 현재까지 확인한 논문 수
        current_citation = citations[i]
        
        # papers_count편의 논문이 각각 current_citation번 이상 인용됨
        # H-Index 조건: h편의 논문이 h번 이상 인용
        if papers_count <= current_citation:
            h_index = papers_count  # 논문 개수가 h_index
        else:
            break  # 더 이상 조건을 만족할 수 없음
            
    return h_index