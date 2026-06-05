class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the array that add up to the target 
        Approach: Use a hash map to track seen numbers and their indices
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}

        for i, num in enumerate(nums):
            corresponding = target - num

            if corresponding in seen:
                return [seen[corresponding], i]
            
            seen[num] = i
