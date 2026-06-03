class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Check if the array contains duplicate elements

        Approach: Use a set to track seen numbers
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
