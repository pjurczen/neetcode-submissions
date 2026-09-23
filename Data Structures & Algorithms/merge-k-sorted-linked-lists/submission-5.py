# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        half: int = len(lists) // 2
        left: ListNode = self.mergeKLists(lists[:half])
        right: ListNode = self.mergeKLists(lists[half:])

        new_head = self.merge(left, right)

        return new_head

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        if left is None:
            return right
        elif right is None:
            return left
        new_head: ListNode
        current: ListNode
        if left.val <= right.val:
            new_head = left
            left = left.next
        else:
            new_head = right
            right = right.next
        current = new_head
        new_head.next = None
        while left or right:
            if right is None or (left is not None and left.val <= right.val):
                current.next = left
                current = left
                left = left.next
            else:
                current.next = right
                current = right
                right = right.next
            current.next = None
        
        return new_head
