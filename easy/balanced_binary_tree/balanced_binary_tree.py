# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is height-balanced
        Approach: Recursive DFS
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def height(node):
            if node is None:
                return 0

            l_height = height(node.left)
            r_height = height(node.right)

            if l_height == -1 or r_height == -1:
                return -1
            if abs(l_height - r_height) >= 2:
                return -1
            else:
                return max(l_height, r_height) +1
        
        return height(root) != -1
