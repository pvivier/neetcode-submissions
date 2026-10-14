# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if head is None:
            return False
        fast = head.next

        if fast is None or fast.next is None:
            return False

        while slow != fast:
            slow = slow.next
            fast = fast.next.next
            if fast is None or fast.next is None:
                return False
        return True