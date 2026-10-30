# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next=head)
        groupPrev = dummy
        groupHead, groupNext = head, head
        while groupHead:
            groupHead = groupNext # 1 | 4
            i: int = 0
            while groupNext and i < k:
                groupNext = groupNext.next
                i += 1
            # groupNext = 4

            if i == k:
                prev, cur = groupNext, groupHead # 1 | 4
                while i > 0: # 3 | 2 | 1
                    tmp = cur.next # 2 | 3 | 4
                    cur.next = prev # 1 -> 4 | 2 -> 1 -> None | 3 -> 2 -> 1 -> None
                    prev = cur # 1 | 2 | 3
                    cur = tmp
                    i -= 1
                    
                groupPrev.next = prev
                groupPrev = groupHead
        
        return dummy.next
