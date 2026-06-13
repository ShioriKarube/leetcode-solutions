# Merge Two Sorted Linked Lists (Easy)

## Problem Description

Merge two sorted linked lists into one sorted linked list and return the head of the merged list

**Example:**

Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]

--- 
## Approach
### Approach: Two pointers
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next
```
- **Time Complexity:** O(n+m)
- **Space Complexity:** O(1)
- **Pros:** Single pass, clean logic, no extra space needed
- **Cons:** Modifies original list structure
---

## Why I Chose This Approach 

Two pointers is the standard approach for merging sorted lists. We compare nodes from both lists and attach the smaller one, moving forward. This guarantees we build a sorted result in one pass without needing extra space for a new list.

---

## Walkthrough (Example) 

Input: list1 = [1,2,4], list2 = [1,3,5]

**Initial state:**
- dummy = [0, next: None]
- current points to dummy

**Step 1:** Compare list1.val and list2.val
- 1 <= 1, so attach list1's node
- current.next = list1
- list1 moves forward to node2
- current moves to node 1
- State: dummy → 1 → 2 → 4

**Step2:** Compare list1.val and list2.val
- 2 > 1, so attach list2's node
- current.next = list2
- list2 moves forward to node3
- current moves to node 1
- State: dummy → 1 → 1 → 3 → 5

**Step 3:** Compare list1.val and list2.val
- 2 <= 3, so attach list1's node
- current.next = list1
- list1 moves forward to node 4
- current moves to node 2
- State: dummy → 1 → 1 → 2 → 4

**Step 4:** Compare list1.val and list2.val
- 4 > 3, so attach list2's node
- current.next = list2
- list2 moves forward to node 5
- current moves to node 3
- State: dummy → 1 → 1 → 2 → 3 → 5

**Step 5:** Compare list1.val and list2.val
- 4 <= 5, so attach list1's node
- current.next = list1
- list1 moves forward to None
- list1 is now empty, loop ends

**Step 6:** Attach remaining nodes
- list1 is None, so attach list2
- current.next = list2
- State: dummy → 1 → 1 → 2 → 3 → 4 → 5

**Return:** dummy.next returns the head node of the merged sorted list

---

## Key Insights
1. Dummy node simplifies logic by giving us a fixed starting point instead of handling the first node separately
2. Two pointers let us track progress in both lists simultaneously and always pick the smaller value
3. When one list runs out, we attach the remaining nodes from the other list since both are already sorted
