# Contains Duplicate (Easy)

## Problem Description
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

**Example:**
- Input: nums = [1, 2, 3, 3]

- Output: true

---
 
## Approach
### Approach: Hash Set (O(n)) 
```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
```

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Pros:** Fast, single pass
- **Cons:** Use extra spaces

---

## Why I Chose This Approach 

Hash set approach is optimal for the following reasons:
1. Set lookup is O(1) on average
2. Single pass through the array is efficient
3. For large arrays (n = 10,000), this approach scales well

---

## Walkthrough (Example)

Input: [1, 2, 3, 1]

| Step | num | seen | Action | Result |
|------|-----|------|--------|--------|
|  1   |  1  |  {}  | 1 not in seen → add 1 | seen = {1} |
|  2   |  2  |  {1} | 2 not in seen → add 2 | seen = {1, 2} |
|  3   |  3  |  {1, 2} | 3 not in seen → add 3 | seen = {1, 2, 3} |
|  4   |  1  |  {1, 2, 3} | 1 in seen | return True

Output: True

---

## Key Insights

1. Set is perfect gor uniqueness problems - O(1) lookup makes checking duplicates fast
2. Early exit saves time - Returning True immediately when a duplicate is found avoids checking the rest
3. Think about edge cases - Empty array and single element returns False
