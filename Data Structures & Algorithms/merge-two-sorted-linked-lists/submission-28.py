# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            list1cursor = list1.next
            list2cursor = list2.next

            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1cursor, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list2cursor, list1)
                return list2 