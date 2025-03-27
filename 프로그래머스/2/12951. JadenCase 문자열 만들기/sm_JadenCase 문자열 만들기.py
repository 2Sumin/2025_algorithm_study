def solution(s):
    arr = []
    words = s.split(' ')
    for word in words:
        arr.append(word.capitalize())
    return ' '.join(arr)
