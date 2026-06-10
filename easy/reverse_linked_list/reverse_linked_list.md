# Reverse Linked List (Easy)

## Problem Description

Given the begining of a singly linked list head, reverse the list and return the new begining of the list.

**Example:**

Input: head = [0,1,2,3]
Output: [3,2,1,0]

--- 
## Approach
### Approach: Three pointer
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        
        return prev
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Pros:** In-place reversal, no extra data struetures needed
- **Cons:** None notable
---

## Why I Chose This Approach

The three pointer method is the standard approach because it reverses pointers in a single pass without creating new nodes or using recursion. It's memory efficient and straightforwar to understand. 

---

## Walkthrough (Example) 

Input: head = [0,1,2,3]

Initial state: prev = None, curr = Node(0)

Iteration 1:
next_node = Node(1)
0.next = None
prev = Node(0), curr = Node(1)

Iteration 2:
next_node = Node(2)
1.next = Node(0)
prev = Node(1), curr = Node(2)

Iteration 3:
next_node = Node(3)
2.next = Node(1)
prev = Node(2), curr = Node(3)

Iteration 4:
next_node = None
3.next = Node(2)
prev = Node(3), curr = None

Loop ends. Return prev = Node(3), which points to the reversd list: [3,2,1,0]

---

## Key Insights
1. Save the next node before reversing the pointer-otherwise you lose the reference to continue traversing
2. The pointer reversal curr.next = prev flips tje direction of the link one node at a time
3. None marks the end of the list and becomes the tail of the reversed list
