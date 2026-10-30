# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode(val=-1, next=head)
        
        l, r = tmp, head
        
        i: int = 0
        while i != n:
            r = r.next
            i += 1
        
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return tmp.next
