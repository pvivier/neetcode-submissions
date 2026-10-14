# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        if node1 is None:
            return node2
        if node2 is None:
            return node1

        if node1.val <= node2.val:
            head = node1
            node1 = node1.next
        else:
            head = node2
            node2 = node2.next
        node = head
        while node1 or node2:
            if node1 and node2:
                if node1.val <= node2.val:
                    node.next = node1
                    node = node1
                    node1 = node1.next
                else:
                    node.next = node2
                    node = node2
                    node2 = node2.next
            elif node1:
                node.next = node1
                node = node1
                node1 = node1.next
            elif node2:
                node.next = node2
                node = node2
                node2 = node2.next

        return head





        






