# Same Binary Tree (Easy)

## Problem Description

Given the roots of two binary trees, p and q, return true if the trees are equivalent, false otherwise. Equivalent means same structure and same node values at every position.

**Example:**

Input: p = [1,2,3], q = [1,2,3]

Output: true

--- 
## Approach
### Approach: 
```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        l_same = self.isSameTree(p.left, q.left)
        r_same = self.isSameTree(p.right, q.right)

        return l_same and r_same
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(h)
- **Pros:** Simple to reason about, mirrors the recursive structure of the problem itself
- **Cons:** Recursion depth grows with tree height
---

## Why I Chose This Approach 

Two trees are the same only if every node matches, all the way down. That's naturally a recursive question: does this node match, and do both of its subtree also match? DFS falls out of the problem definition instead of being tacked on.

---

## Walkthrough (Example) 

Input: p = [1,2,3], q = [1,2,3]

isSameTree(1, 1) → value match → recurse left and right

- left: isSameTree(2, 2) → values match, both children None → True
- right: isSameTree(3, 3) → values match, both children None → True

Root: l_same = True, r_same = True → l_same and r_same → True

---

## Key Insights
1. Any mismatch returns False immediately - no reason to keep comparing once one pair disagrees
2. l_same and r_same is not the same as l_same == r_same when both are False. False == False → True
3. Base cases have to run before p.val != q.val, otherwise comparing .val on a None node throws and AttributeError
