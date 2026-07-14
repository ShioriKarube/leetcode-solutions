# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees, determine if they are structurally identical with matching node values
        Approach: Recursive DFS
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        l_same = self.isSameTree(p.left, q.left)
        r_same = self.isSameTree(p.right, q.right)

        return l_same and r_same
