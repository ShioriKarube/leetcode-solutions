# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Find the longest path between any two nodes in a binary tree
        Approach: Iterative Post-order traversal
        Time Complexity: O(n)
        Space Complexity: O(n) 
        """
        depth = {None: 0}
        diameter = 0

        stack = []
        node = root
        last = None

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack[-1]
                if peek.right and last != peek.right:
                    node = peek.right
                else:
                    left = depth[peek.left]
                    right = depth[peek.right]
                    diameter = max(diameter, left + right)
                    depth[peek] = max(left, right) + 1
                    last = stack.pop()

        return diameter
