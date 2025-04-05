def solution(n):

    # result =[]
    # i = 0

    # while i < n :
        # if i % 2 == 0:
            #result.append("수")
        # else :
            # result.append("박")

        # i += 1

    # return ''.join(result)
     return ''.join(["수" if i % 2 ==0 else "박" for i in range(n)])
