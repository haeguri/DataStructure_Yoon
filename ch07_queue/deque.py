class Node():

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque():

    def __init__(self):
        self.head = None
        self.tail = None

    def dq_add_first(self, data):
        new_node = Node(data)

        new_node.next = self.head

        if self.dq_is_empty():
            self.tail = new_node
        else:
            self.head.prev = new_node

        self.head = new_node

    def dq_add_last(self, data):
        new_node = Node(data)

        new_node.prev = self.tail

        if self.dq_is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    def dq_remove_first(self):

        if self.dq_is_empty():
            print("삭제할 노드가 없습니다.")
            return None

        rpos = self.head
        rdata = self.head.data

        if self.head == self.tail:
            # self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            # self.head = self.head.next

        self.head = self.head.next

        del rpos

        return rdata

    def dq_remove_last(self):

        if self.dq_is_empty():
            print("삭제할 노드가 없습니다.")
            return None

        rpos = self.tail
        rdata = self.tail.data

        if self.head == self.tail:
            self.head = None
            # self.tail = None
        else:
            self.tail.prev.next = None
            # self.tail = self.tail.prev

        self.tail = self.tail.prev

        del rpos

        return rdata

    def dq_get_first(self):

        if self.dq_is_empty():
            print("조회할 노드가 없습니다.")
            return None

        return self.head.data

    def dq_get_last(self):

        if self.dq_is_empty():
            print("조회할 노드가 없습니다.")
            return None

        return self.tail.data

    def dq_is_empty(self):
        if self.head is None:
            return True
        else:
            return False