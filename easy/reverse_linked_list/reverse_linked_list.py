# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """"
        Reverse a singly linked list by iterating through and reversing pointers
        Approach: Three pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        
        return prev
