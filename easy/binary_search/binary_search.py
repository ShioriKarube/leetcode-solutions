class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Find the index of a target value in a sorted array. Return -1 if not found.
        Approach: Binary search
        Time Complexity: O(logn)
        Space Complexity: O(1)
        """
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
