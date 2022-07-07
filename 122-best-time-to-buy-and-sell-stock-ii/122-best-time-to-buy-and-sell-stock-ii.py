class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_so_far = 0
        for i in range(len(prices)-1):
          if prices[i+1]-prices[i]> 0:
            profit_so_far += prices[i+1]-prices[i]
        return profit_so_far
        