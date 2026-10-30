# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode(val=-1, next=head)
        prev, cur, next = tmp, head, head.next

        count = 0
        counter = head
        while counter:
            count += 1
            counter = counter.next

        targetIdx = count - n

        i: int = 0
        while i != targetIdx:
            prev = cur
            cur = next
            next = next.next if next else None
            i += 1
        
        prev.next = next
        cur.next = None

        return tmp.next
