# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_head = head
        while head:
            next_node = head.next
            if next_node:
                new_head = ListNode(val=next_node.val, next=new_head)
                head.next = None
            head = next_node
        return new_head
