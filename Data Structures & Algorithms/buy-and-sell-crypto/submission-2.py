class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_profit=0
        l=len(prices)
        i=0
        while i < l:
                min_price=min(min_price,prices[i])
                max_profit=max(max_profit,prices[i]-min_price)
                i+=1
        return max_profit

        