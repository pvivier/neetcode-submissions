# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node1 = l1
        node2 = l2
        while node1 or node2:
            node1.val = node1.val + node2.val
            if node1.val >= 10:
                node1.val = node1.val - 10
                if node1.next:
                    node1.next.val = node1.next.val + 1
                else:
                    node = ListNode(1)
                    node1.next = node
            if not node1.next and not node2.next:
                return l1
            if not node1.next:
                node1.next = ListNode(0)
            if not node2.next:
                node2.next = ListNode(0)
            node1 = node1.next
            node2 = node2.next