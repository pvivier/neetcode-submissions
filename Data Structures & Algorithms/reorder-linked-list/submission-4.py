# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev_node = None
        current_node = slow.next
        slow.next = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        node1 = head
        node2 = prev_node
        

        while node2:
            prev_next1 = node1.next
            # print('node1')
            # print(node1.val)
            # print(prev_next1.val)
            prev_next2 = node2.next

            # print('node2')
            # print(node2.val)
            # print(prev_next2.val)
            node1.next = node2
            node2.next = prev_next1

            node1 = prev_next1
            node2 = prev_next2








        

