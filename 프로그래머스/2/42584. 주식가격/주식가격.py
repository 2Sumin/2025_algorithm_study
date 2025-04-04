def solution(prices):
    ans = [0]*len(prices)
    for i in range(len(prices)):
        curr_price = prices[i]
        for j in range(i+1, len(prices)):
            if prices[j] < curr_price:
                ans[i] = j-i
                break
            elif j == len(prices)-1:
                ans[i] = j-i

    return ans