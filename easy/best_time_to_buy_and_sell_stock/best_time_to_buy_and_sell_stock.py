class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Given an array of prices, find the maximum profit you can achieve
        by buying on one day and selling on a later day. If no transactions are made,
        return 0.
        Approach: Single pass with min tracking
        Time Complexity: O(n)
        Space Complexity:O(1)
        """
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
