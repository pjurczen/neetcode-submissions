# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListIterative(head)
    
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        old_head = head
        new_head = None
        while old_head:
            next_node = old_head.next
            old_head.next = new_head
            new_head = old_head
            old_head = next_node
        return new_head
    # None, 0, 1, 2, 3
    # 0, None    1, 2, 3
    # 1, 0, None   2, 3

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        if head.next:
            new_head = self.reverseListRecursive(head.next)
            head.next.next = head
            head.next = None
        else:
            new_head = head
        
        return new_head
