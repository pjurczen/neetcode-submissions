# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(val=-1)
        prev, cur = tmp, None

        rest = 0
        while l1 or l2 or rest:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            cur = ListNode(val=l1val + l2val + rest)
            prev.next = cur
            rest = 0
            if cur.val > 9:
                cur.val = cur.val % 10
                rest = 1
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            prev = cur
            cur = None
        
        return tmp.next
            