from ch04_linkedlist2.node import Node

class BasedLinkedList():
    head = None

    def __init__(self):
        self.head = None

    def SPush(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def SPop(self):
        if self.SIsEmpty():
            print("꺼낼 데이터가 없습니다.")
            return None

        rdata = self.head.data
        rpos = self.head

        self.head = self.head.next
        del rpos

        return rdata

    def SPeek(self):
        if self.SIsEmpty():
            print("참조할 데이터가 없습니다.")
            return None

        return self.head.data

    def SIsEmpty(self):
        if self.head is None:
            return True
        else:
            return False