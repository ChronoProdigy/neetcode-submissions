class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        sell = 0
        buy = 0
        if len(prices) < 2:
            return maxProfit
        elif len(prices) == 2 and prices[1] > prices[0]:
            return prices[1]-prices[0]
        elif len(prices) == 2 and prices[1] < prices[0]:
            return 0

        for i in range(len(prices)-1, 0, -1):
            if prices[i] > sell:
                sell = prices[i]
            buy = prices[i-1]
            profit = sell - buy
            if profit > maxProfit:
                maxProfit = profit
            
        print(sell)
        print(buy)
        return maxProfit