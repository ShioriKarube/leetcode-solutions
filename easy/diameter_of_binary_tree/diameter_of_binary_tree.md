# Diameter of Binary Tree (Easy)

## Problem Description

Find the longest path between any two nodes in a binary tree.

**Example:**

Input: root = [1,null,2,3,4,5]

Output: 3

--- 
## Approaches
### Approach 1: Iterative Post-order Traversal 
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
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
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Pros:** Guaranteed O(n) space complexity, no risk of stack overflow
- **Cons:** More verbose, harder to read
---

### Approach 2: Recursive DFS
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        dfs(root)
        return self.diameter
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(h)
- **Pros:** Clean and concise
- **Cons:** Risk of stack overflow on very deep trees
---

## Why I Chose This Approach 

Approach 1 guarantees O(n) space regardless of tree shape avoiding stack overflow on skewed trees.

---

## Walkthrough (Example) 

Input: root = [1,null,2,3,4,5]

**Start:** `stack = []`, `node = 1`, `last = None`, `depth = {None: 0}, `diameter = 0`

**Phase 1 - traverse left spine of right subtree (push 1→2→3→5):**
- node=1 → push. stack=[1], node=1.left=None
- node=None → peek=1, right=2, last≠2 → node=2
- node=2 → push. stack=[1,2], node=2.left=3
- node=3 → push. stack=[1,2,3], node=3.left=5
- node=5 → push. stack[1,2,3,5], node=5.left=None

**Process node5** (no right child):
- left=depth[None]=0, right=depth[None]=0
- diameter=max(0, 0+0)=0, depth[5]=1
- last=5, stack=[1,2,3]

**Process node3** (right=None):
- left=depth[5]=1, right=depth[None]=0
- diameter=max(0, 1+0)=1, depth[3]=2
- last=3, stakcj[1,2]

**Phase 2 - move to right subtree of node 2:**
- peek=2, right=4, last(3)≠4 → node=4
- node=4 → push. stack=[1,2,4], node=4.left=None

**Process node 4** (no children):
- left=depth[None]=0, right=depth[None]=0
- diameter=max(1, 0+0)=1, depth[4]=1
- last=4, stack=[1,2]

**Process node 2** (last==right==4, so pop):
- left=depth[3]=2, right=depth[None]=0
- diameter=max(1, 2+1)=**3**, depth[2]=3
- last=2, stack=[1]

**Process node 1** (last==right==2, so pop):
- left=depth[None]=0, right=depth[2]=3
- diameter=max(3, 0+3)=3, depth[2]=3
- last=2, stack=[]

Stack is empty → `return 3`

---

## Key Insights
1. At each node, the longest path through it = left depth + right depth
2. The diameter doesn't have to pass through the root - track the global max separately
