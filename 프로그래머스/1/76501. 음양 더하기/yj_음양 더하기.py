 # idx 활용 
    # 인덱스 확인 후 t는 덧셈, f는 뺄셈 연산하기
    return sum(absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes)))

