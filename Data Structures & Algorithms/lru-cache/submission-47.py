class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.running_capacity = 0
        self.dic = {}
        self.node_dic = {}
        self.head = ListNode()
        self.last = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            current = ListNode(key)
            self.last.next = current
            current.prev = self.last
            self.last = current
            if self.head.val == key:
                self.head = self.head.next
            else:
                node_to_remove = self.node_dic[key]
                node_to_remove.prev.next = node_to_remove.next
                node_to_remove.next.prev = node_to_remove.prev
            self.node_dic[key] = current
        return self.dic.get(key, -1)

    def put(self, key: int, value: int) -> None:
        current = ListNode(key)
        self.last.next = current
        current.prev = self.last
        self.last = current
        if not self.head.val:
            self.head = self.head.next
            
        if key not in self.dic:
            if self.running_capacity < self.capacity:
                self.running_capacity += 1
            else:
                key_to_delete = self.head.val
                del self.dic[key_to_delete]
                self.head = self.head.next
        else:
            if self.head.val == key:
                self.head = self.head.next
            else:
                node_to_remove = self.node_dic[key]
                node_to_remove.prev.next = node_to_remove.next
                node_to_remove.next.prev = node_to_remove.prev
        self.dic[key] = value
        self.node_dic[key] = current
        
        node = self.head
        while node:
            print(node.val)
            node = node.next
