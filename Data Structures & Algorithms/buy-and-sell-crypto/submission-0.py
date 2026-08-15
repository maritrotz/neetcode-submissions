class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,1
        profit = 0

        while j <= len(prices) - 1 and i<j:
            profit = max(profit,prices[j]-prices[i])
            if prices[i] > prices[j]:
                i = j
                j = j+1
            else:
                j = j + 1
        return profit

        