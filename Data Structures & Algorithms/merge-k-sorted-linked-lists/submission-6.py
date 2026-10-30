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

        half = len(lists) // 2
        left = self.mergeKLists(lists[:half])
        right = self.mergeKLists(lists[half:])

        return self.merge(left, right)


    def merge(self, left: Optional[ListNode], right: Optional[ListNode]):
        if not right:
            return left
        elif not left:
            return right
        
        newHead = None
        current = None
        if left.val <= right.val:
            newHead = left
            left = left.next
        else:
            newHead = right
            right = right.next
        
        current = newHead
        current.next = None

        while left or right:
            if right is None or (left is not None and left.val <= right.val):
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
            current.next = None

        return newHead

