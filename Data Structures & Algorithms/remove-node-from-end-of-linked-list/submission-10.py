# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        count = 1
        while count < n:
            fast = fast.next
            count+=1
        print('fast.val')
        print(fast.val)
        dummy = ListNode()
        slow = dummy
        slow.next = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next