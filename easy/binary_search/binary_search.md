# Binary Search (Easy)

## Problem Description

Find the index of a target value in a sorted array of distinct integers. Return -1 if the target does not exist.

**Example:**

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3

--- 
## Approach
### Approach: Binary search 
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
```
- **Time Complexity:** O(logn)
- **Space Complexity:** O(n)
- **Pros:** Optimal for sorted arrays; guaranteed to find the target if it exists. Efficient even for large inputs
- **Cons:** Requiers the array to be sorted beforehand. Cannot be applied to unsorted data without preprocessing
---

## Why I Chose This Approach 

The problem requires O(logn) time complexity, which eliminates linear search. Binary search is the standard and only viable approach for sorted arrays when logarithmic performance is mandatory. By comparing the middle element with the target and eliminating half of the remaining search space on each iteration, the algorithm achieves optimal efficiency.

---

## Walkthrough (Example) 

Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3

Iteration 1:
l=0, r=5, mid=2
nums[2] = 2 < target → search right half
Update: l=3

Iteration 2:
l=3, r=5, mid=4
nums[4] = 6 > target → search left haf
Update: r=3

Iteration 3:
l=3, r=3, mid=3
nums[3] = 4 == target → found
Return 3

---

## Key Insights
1. Comparing the middle element with the target determines which half of the array to eliminate, reducing the search logarithmically
2. The condition l <= r ensures the last remaining element is checked before termination
3. Binary search requires a sorted array; the sorted property is essential to guarantee correctness
