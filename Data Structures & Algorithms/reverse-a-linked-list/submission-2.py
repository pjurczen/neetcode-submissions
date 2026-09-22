# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListRecursive(head)
    
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_head = None
        while head:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node
        return new_head

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
