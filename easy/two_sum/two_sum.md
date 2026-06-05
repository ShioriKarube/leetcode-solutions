# Two Sum

## Problm Description

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

**Example:**

Input: nums = [3,4,5,6], target = 7

Output: [0,1]

--- 
## Approaches
### Approach: Hash Map
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            corresponding = target - num

            if corresponding in seen:
                return [seen[corresponding], i]
            
            seen[num] = i
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Pros:** Single pass through the array; efficient lookup with hash map
- **Cons:** Use extra sppace proportional to input size
---

## Why I Chose This Approach 

The hash map approach is the optimal solution for this problem. Rather than checking every pair (which the space complexity would be O(n^2)), we use the complementary number strategy. 

---

## Walkthrough (Example) 

Input: `nums = [3,4,5,6]`, `target = 7`

1. **i=0, num=3**: `corresponding: 7 - 3 = 4`. Not in `seen`. Add `{3: 0} to `seen`.
2. **i=1, num=4**: `corresponding: 7 - 4 = 3`. Found in `seen`. Return `[seen[3], 1] = `[0, 1]`

---

## Key Insights

1. Complementary number strategy: Instead of checking all pairs, we break down the problem into "what number do I need to complete the target sum?". This flips the time complexity from O(n^2) to O(n).
2. Single pass: We build the map as we go, so we never need a second loop through the data.
3. Index ordering: The smaller index is automatically returned because we only store numbers we've already seen. The current index `i` is always larger than `seen[corresponding]`.
