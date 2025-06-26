def solution(clothes):
    
    # 하루에 최소한 한개의 의상입음. 
    # 2차원 배열 : 의상의 이름 x 의상의 종류 
    
    dict_clothes = {}
    total = 1 
    # clothes 배열 돌면서 해시 딕셔너리를 완성하기 (키 - 옷의 종류 / 값 - 해당 종류 옷의 개수 )
    for c_name, c_type in clothes: 
        if c_type in dict_clothes:
            dict_clothes[c_type] += 1
        else : 
            dict_clothes[c_type] = 1
            
    # 경우의 수 문제이므로 각 키별 값 + 1 해서 다 곱하기 
    for i in dict_clothes.values():
        total *= (i+1)
        
    
    # 결과에서 1 뺌 (나체 상태 제외)
    return total-1
