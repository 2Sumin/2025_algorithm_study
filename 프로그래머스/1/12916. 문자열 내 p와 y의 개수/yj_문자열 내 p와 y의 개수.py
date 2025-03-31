def solution(s):
    
    s = s.casefold()
    
    if s.count("p") == s.count("y"):
        return True
    else:
        return False
