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
        self.head = ListNode(-1)
        self.last = self.head
        self.first_loop = 0

    def get(self, key: int) -> int:

        # if the key is not in the dic, return -1

        # if it is in the dic,
        # find its value and return it, but also update the linked list
        if key in self.dic:
            current = ListNode(key)
            self.last.next = current
            current.prev = self.last
            self.last = current

            if self.head.val == key:
                self.head = self.head.next
            else:
                node_to_remove = self.node_dic[key]
                print('in ' + str(node_to_remove.val))
                print('in ' + str(node_to_remove.prev.val))
                print('in ' + str(node_to_remove.next.val))
                node_to_remove.prev.next = node_to_remove.next
                node_to_remove.next.prev = node_to_remove.prev
            self.node_dic[key] = current
            print('blue' + str(current.val))

        print('getting', key)
        node = self.head
        while node:
            print(node.val)
            node = node.next

        return self.dic.get(key, -1)

    def put(self, key: int, value: int) -> None:
        print('putting', value)
        current = ListNode(key)
        self.last.next = current
        current.prev = self.last
        self.last = current

        if key not in self.dic:
            if self.running_capacity < self.capacity:
                self.running_capacity += 1
            else:
                key_to_delete = self.head.val
                del self.dic[key_to_delete]
                self.head = self.head.next
            self.dic[key] = value
            self.node_dic[key] = current
        else:
            if self.head.val == key:
                self.head = self.head.next
            else:
                node_to_remove = self.node_dic[key]
                node_to_remove.prev.next = node_to_remove.next
                node_to_remove.next.prev = node_to_remove.prev
            self.dic[key] = value
            self.node_dic[key] = current
        if self.head.val == -1:
            if self.first_loop == 0:
                self.head = self.head.next
                self.first_loop = 1
        node = self.head
        while node:
            print(node.val)
            node = node.next
            # first you create a listnode CURRENT with that key
        # it will go at the end of the list whatevery happens

        # is the key in the normal dic?
        # 0- if it isnt
        # you check if you need to delete because there are already 10 objects
        # you check by checking if the running capacity == capacity

        # 0.0 you dont need to delete
        # you dont do anything unique except add 1 to running capacity
        # 0.1 you do need to delete
        # you find the head of the list
        # that head has as a value the key to delete
        # you delete that key in the dic
        # you set head = head.next

        # 1 the key is already in the dic
        # you need to remove it from the linked list
        # you find the node in the linked list using node_dic[key]
        # you set node.prev.next = node.next

        # at the end of all this:
        # you add this key to the normal dic, with the value
        # you add this key to the node dic, with the listnode
        # you point last.next to this node and node.prev to last
        # you set last = node


