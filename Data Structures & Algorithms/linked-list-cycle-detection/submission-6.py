# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        while fast and fast.next:
            if slow == fast.next or slow == fast.next.next:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False
        