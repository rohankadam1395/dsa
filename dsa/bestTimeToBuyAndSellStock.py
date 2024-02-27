def maxProfit(prices):
    print(prices)
    # max_profit = 0 
    # for i in range(len(prices)):
    #     print(prices[i])
    #     for j in range(i+1,len(prices)):
    #         print(prices[j])
    #         profit = prices[j] - prices[i]
    #         if profit > max_profit:
    #             max_profit = profit
    #     print("----------")
    # return max_profit
    chepaest_price = prices[0]
    max_profit = 0 
    for i in range(1,len(prices)):
        if prices[i] < chepaest_price:
            chepaest_price = prices[i]
        else:
            profit = prices[i] - chepaest_price
            if profit > max_profit:
                max_profit = profit
    return max_profit





print(maxProfit([7,1,5,3,6,4]))



