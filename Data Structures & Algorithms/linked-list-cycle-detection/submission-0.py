# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_ = set()

        node = head
        while node:
            if node in set_:
                return True
            set_.add(node)
            node = node.next
        return False