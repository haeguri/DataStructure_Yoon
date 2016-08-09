from ch04_linkedlist2.node import Node

class ListBaseQueue():
    front = None
    rear = None

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("삭제할 노드가 없습니다.")
            return None

        rpos = self.front
        rdata = self.front.data

        self.front = self.front.next

        del rpos
        return rdata

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def q_peek(self):
        if self.is_empty():
            print("조회할 노드가 없습니다.")
            return None

        return self.front.data