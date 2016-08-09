from ch05_linkedlist3.node import Node

class CircleLinkedList():
    tail = None
    cur = None
    before = None
    num_of_data = None

    def __init__(self):
        self.tail = None
        self.num_of_data = 0

    # 노드를 머리(tail.next)에 추가.
    def LInsertFront(self, data):

        new_node = Node(data)

        # 첫 번째 노드?
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

        self.num_of_data += 1

    def LInsert(self, data):
        new_node = Node(data)

        # 첫 번째 노드?
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

        self.num_of_data += 1

    def LFirst(self):
        if self.tail is None:
            print("조회할 노드가 없습니다.")
            return None

        self.cur = self.tail.next
        self.before = self.tail

        return self.cur

    def LNext(self):
        if self.cur.next is None:
            print("조회할 노드가 없습니다.")
            return None

        self.before = self.cur
        self.cur = self.cur.next

        return self.cur

    def LRemove(self):
        if self.tail is None:
            print("삭제할 노드가 없습니다.")
            return None

        if self.cur == self.cur.next:
            self.tail = None
        else:
            self.before.next = self.cur.next
            self.cur = self.before

        self.num_of_data -= 1

        return True

    def LCount(self):
        return self.num_of_data