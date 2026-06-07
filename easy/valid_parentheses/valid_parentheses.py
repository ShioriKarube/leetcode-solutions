class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check if a string of brackets is valid (properly opened and closed).
        Approach: Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for char in s:
            if char in brackets:
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)

        return not stack
