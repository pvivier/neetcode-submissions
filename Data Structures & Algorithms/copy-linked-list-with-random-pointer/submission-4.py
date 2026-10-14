"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return

        prev_node = head
        new_prev_node = Node(head.val)
        head2 = new_prev_node

        new_prev_node.match = prev_node
        prev_node.match = new_prev_node

        while prev_node.next:
            node = prev_node.next
            new_node = Node(node.val)
            new_prev_node.next = new_node
            
            new_node.match = node
            node.match = new_node

            prev_node= node
            new_prev_node = new_node

        #return head2
        node = head2

        while node:
            if node.match.random:
                node.random = node.match.random.match
            else:
                node.random = None
            node = node.next
        return head2


