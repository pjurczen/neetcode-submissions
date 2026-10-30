# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newHead = None
        prevTail = None
        groupCur = head
        while groupCur:
            nextGroup = groupCur # 1
            i: int = 0
            while nextGroup and i < k:
                nextGroup = nextGroup.next
                i += 1
            # 4

            if i == k:
                curHead = groupCur # 1 | 4
                cur = groupCur # 1 | 4
                prev, next = None, None
                while i > 0: # 3 | 2 | 1
                    next = cur.next # 2 | 3 | 4
                    cur.next = prev # 1 -> None | 2 -> 1 -> None | 3 -> 2 -> 1 -> None
                    prev = cur # 1 | 2 | 3
                    cur = next
                    i -= 1
                curHead.next = cur # 1 -> 4
                if not newHead:
                    newHead = prev # 3
                if prevTail:
                    prevTail.next = prev
                prevTail = curHead

            groupCur = nextGroup # 4
        
        return newHead
