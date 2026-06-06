# Best Time to Buy and Sell Stock (Easy)

## Problem Description

You are given an array of integers prices, where prices[i] is the price of a stock on day i. You can buy on one day and sell on a later day. Find the maximum profit possible. If you do not make any transaction, return 0.

**Example:**

Input: prices = [10,1,5,6,7,1]

Output: 6

--- 
## Approach
### Approach: Single pass with min tracking
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Pros:** Simple one-pass solution. No need to store anything except the maximum profit and the cheapest price seen so far.
- **Cons:** Only works if you need one pair of sell and buy. Doesn't handle multiple transaction.
---

## Why I Chose This Approach 

Track the lowest price encountered so far, then calculate the profit at each step by subtracting that minimum price from the current price. This eliminates the need for nested loops or tracking multiple pairs-the maximum profit emerges naturally from a single pass through the array.

---

## Walkthrough (Example) 

prices = [7, 1, 5, 3]

Day 0: price = 7
    min_price = 7, profit = 0, max_profit = 0
Day 1: price = 1
    min_price = 1, profit = 0, max_profit = 0
Day 2: price = 5
    min_price = 1, profit = 4, max_profit = 4
Day 3: price = 3
    min_price = 1, profit = 2, max_profit = 4

The answer is 4 (buy on day1, sell on day2)
---

## Key Insights
1. You need to track the lowest price we've seen, not all previous prices. The best profit at any point is determined by today's price minus the lowest price we've passed.
2. If prices keep dropping, we will never make a profit. The algorithm naturally returns 0 in that case because max_profit never gets updated.
