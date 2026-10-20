from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = deque()
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        while slow:
            stack.append(slow.val)
            slow = slow.next
        result = 0
        left = head
        while stack:
            right = stack.pop()
            result = max(result, left.val + right)
            left = left.next
        return result

