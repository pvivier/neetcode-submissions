# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        node = head
        while node is not None:
            node = node.next
            length +=1
        if length==1:
            return
        middle = length //2
        node = head
        count = 1
        while count <= middle:
            if count == middle:
                head2 = node.next
                node.next = None
                count+=1
            else:
                node = node.next
                count+=1

        prev_node = None
        current_node = head2
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        node1 = head
        node2 = prev_node

        while node1.next:
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

        if node2:
            node1.next = node2







        

