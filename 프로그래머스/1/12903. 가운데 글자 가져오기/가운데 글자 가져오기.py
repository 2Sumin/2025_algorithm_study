def solution(s):
    mid = len(s)//2
    if mid == len(s)/2:
        return s[mid-1:mid+1]
    else:
        return s[mid]