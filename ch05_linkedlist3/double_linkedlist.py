from ch05_linkedlist3.node2 import Node2 as Node

class DoubleLinkedList():
    head = None
    tail = None
    cur = None
    num_of_data = None

    def __init__(self):
        dmy1 = Node(None)
        dmy2 = Node(None)

        self.head = dmy1
        self.tail = dmy2

        self.head.next = self.tail
        self.tail.prev = self.head
        self.num_of_data = 0

    # head -> dmy -> dmy <- tail
    # dmy -> newnode -> dmy
    def LInsert(self, data):
        new_node = Node(data)

        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        self.tail.prev = new_node
        new_node.next = self.tail

        self.num_of_data += 1

    def LFirst(self):
        if self.head.next is None:
            print("연결리스트가 비어 있습니다.")
            return None

        self.cur = self.head.next

        return self.cur

    def LNext(self):
        if self.cur.next.data is None:
            print("맨 마지막 노드입니다.")
            return None

        self.cur = self.cur.next

        return self.cur

    def LRemove(self):
        if self.cur.data is None or self.num_of_data == 0:
            print("연결리스트가 비어 있어 삭제할 수 없습니다.")

        rpos = self.cur
        self.cur.prev.next = self.cur.next
        self.cur.next.prev = self.cur.prev
        self.cur = self.cur.prev

        del rpos
        self.num_of_data -= 1

    def LCount(self):
        return self.num_of_data