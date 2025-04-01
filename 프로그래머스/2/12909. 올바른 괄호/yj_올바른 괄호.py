stack = []
    
    for par in s :
        if par =='(':
            stack.append(par)
        elif par ==')':
            if not stack:
                return False # 스택 비어 있음 (닫는게 먼저 온거임)
            stack.pop()  
    return len(stack) == 0
