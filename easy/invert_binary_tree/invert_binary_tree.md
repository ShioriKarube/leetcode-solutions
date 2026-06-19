# Invert Binary Tree (Easy)

## Problem Description

Given the root of a binary tree, swap the left and the right children of every node

**Example:**

Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]

---
## Approach
### Approach 1: Iterative BFS
```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Pros:** No recursion, so no risk of hitting Python's call stack limit on very deep trees
- **Cons:** Slightly more code than the recursive version
---

### Approach 2: Recursive DFS

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)
- **Pros:** Clean and short
- **Cons:** Deep trees can hit Python's recursion limit
---

## Why I Chose This Approach 

BFS makes the level-by-level processing explicit, which makes it easer to reason about. The recursive version is shorter, but the call stack is hidden-BFS puts the queue right in front of you

## Walkthrough (Example) 

Input: root = [1,2,3,4,5,6,7]

queue = [1]

Step 1: pop node 1
- swap: left=3, right=2
- add 3 and 2 to queue
- queue = [3,2] 

Step 2: pop node 3
- swap: left=7, right=6
- add 7 and 6 to queue
- queue = [2,7,6]

Step 3: pop node 2
- swap: left=5, right=4
- add 5 and 4 to queue
- queue = [7,6,5,4]

Step 4: pop node 7
- no children, nothing to add
- queue = [6,5,4]

Step 5: pop node 6
- no children, nothing to add
-queue = [5,4]

Step 6: pop node 5
- no children, nothing to add
- queue = [4]

Step 7: pop node 4
- no children, nothing to add
- queue = []

queue is empty, loop ends. Return root

Output: [1,3,2,7,6,5,4]

---

## Key Insights
1. Every node needs its children swapped exactly once-visiting each node once is enough
2. BFS and DFS both work here. The difference is space: BFS uses O(n) explicitly via the quere; DFS uses O(h) implicitly via the call stack
