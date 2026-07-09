# Balanced Binary Tree (Easy)

## Problem Description

Given a bianry tree, return true if every node's left and right subtrees differ in height by no more than 1  

**Example:**

Input: root = [1,2,3,null,null,4]

Output: true

--- 
## Approach
### Approach: Recursive DFS
```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
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

```
- **Time Complexity:** O(n)
- **Space Complexity:** O(h)
- **Pros:** Single pass; no redundant height calculations
- **Cons:** Recursive - very deep skewed trees could cause a stack overflow
---

## Why I Chose This Approach 

The native approach would calcualte height separately for every node, visiting nodes repeatedly and resulting in O(n^2). By returning -1 as a warning signal when an imbalance is detected, we can combine the height calculation and balance check into a single bottom-up pass, achieving O(n).

---

## Walkthrough (Example) 

root = [1,2,3,null,null,4]

Start: height(1) is called → recurses all the way down before returning anything

Process node 4 (no children):
- l_height = height(None) = 0, r_height = height(None) = 0
- abs(0 - 0) = 0 → balanced
- returns max(0, 0) + 1 = 1

Process node 2 (no children):
- l_height = height(None) = 0, r_height = height(None) = 0
- abs(0 - 0) = 0 → balanced
- returns max(0, 0) + 1 = 1

Process node 3 (left child = 4):
- l_height = height(4) = 1, r_height = height(None) = 0
- abs(0 - 1) = 1 → balanced
- returns max(0, 1) + 1 = 2

Process node 1 (root):
- l_height = height(2) = 1, r_height = height(3) = 2
- abs(1 - 2) = 1 → balanced
- returns max(1, 2) + 1 = 3

- height(root) != -1 → 3 != -1 → True

---

## Key Insights
1. Real heights are always >= 0, so -1 is safe to use as a warning signal - it can never be confused with an actual height
2. Checking l_height == -1 or r_height == -1 before doing any match ensure the warning signal travels up cleanly without getting destroyed by arithmetic
3. Post-order traversal (left → righ → nodeis the natural fit here - a node can only check its own balance after both children have reported back
