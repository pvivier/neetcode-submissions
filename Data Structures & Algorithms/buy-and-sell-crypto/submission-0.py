class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minimum = prices[0]
        profit = 0

        for p in prices:
            if p < minimum:
                minimum = p
            profit = max(profit,p - minimum)
        return profit