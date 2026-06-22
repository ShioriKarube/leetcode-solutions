# Maximum Depth of a Binary Tree (Easy)

## Problem Description

Given a binary tree, find its maximum depth - the number of nodes along the longest path from the root to the farthest leaf.

**Example:**

Input: root = [1,2,3,null,null,4]

Output: 3

---
## Approaches
### Approach 1: BFS (Iterative)
```python
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Pros:** Space complexity is explicity and predictible; no risk of stack overrflow on very deep trees
- **Cons:** Slightly more code than the recursive version
---

### Approach 2: DFS (Recursive)
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(h)
- **Pros:** Clean and concise; the logic maps directly to the definition of depth
- **Cons:** Risk of stack overflow on extremely deep trees
---

## Why I Chose This Approach 

BFS processes the tree level by level, so incrementing depth once per level is natural. The recursive DFS version is shorter, but BFS makes the O(n) space usage explicit - which is what the problem asks for.

---

## Walkthrough (Example) 

Input: root = [1,2,3,null,null,4]

**Start:** `queue = [1]`, `depth = 0`

**Loop 1 - process level 1 (node 1):**
- Pop node 1. Add its children: 2 and 3
- `queue = [2,3]`, `depth=1`

**Loop 2 - process level 2 (nodes 2, 3):**
- Pop node 2. No children, nothing added
- Pop node 3. Add its left child: 4
- `queue = []`, `depth=2`

**Loop 3 - process level 3 (node 4):**
- Pop node 4. No children, nothid added
- `queue = []`, `depth=3`

Queue is empty → `return 3`

---

## Key Insights
1. `for _ in range(len(queue))` is the key  Snapshotting the queue size at the start of each loop means only the current level gets processed - nodes added during the loop belong to the next level.
2. BFS depth = number of levels processed. Incrementing `depth` once per outer loop iteration is all that's needed.
3. Both BFS and DFS visit every node exactly once, so time complexity is O(n) either way. The difference is where the space goes: BFS uses an explicit queue, DFS uses the call stack.
