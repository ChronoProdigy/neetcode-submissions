# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        i = 0
        if head is None:
            return False
        while head.next:
            if head.val in seen:
                return True
            seen[head.val] = i
            i += 1
            head = head.next
        return False
