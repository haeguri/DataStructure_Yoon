from ch04_linkedlist2.node import Node
import ctypes

class DLinkedList():
    head = None
    cur = None
    before = None
    num_of_data = None
    comp = None

    # 더미 노드에 데이터가 None? C 에서도?
    def __init__(self):
        new_node = Node(None)
        # head가 더미 노드를 가르키도록.
        self.head = new_node
        self.num_of_data = 0

    def f_insert(self, data):
        new_node = Node(data)

        new_node.next = self.head.next
        self.head.next = new_node

        self.num_of_data += 1

    # 정렬
    # 정렬 기준이 있을 때의 삽입
    def s_insert(self, data):
        new_node = Node(data)

        pred = self.head

        while pred.next is not None and self.comp(data, pred.next.data) != 0:
            pred = pred.next

        new_node.next = pred.next
        # print("self.head", id(self.head))
        # print("pred     ", id(pred))
        pred.next = new_node
        # print("self.head", id(self.head))
        # print("pred     ", id(pred))

        self.num_of_data += 1

    def l_insert(self, data):
        if self.comp is None:
            self.f_insert(data)
        else:
            self.s_insert(data)

    def l_first(self):
        if self.head.next is None:
            print("조회할 노드가 없습니다.")
            return None

        self.before = self.head
        self.cur = self.head.next

        return self.cur

    def l_next(self):
        if self.cur.next is None:
            print("마지막 노드입니다.")
            return None

        self.before = self.cur
        self.cur = self.cur.next

        return self.cur

    def l_remove(self):
        # rpos = self.cur
        rdata = self.cur.data

        self.before.next = self.cur.next
        del self.cur
        # self.cur = self.before

        # del rpos
        self.cur = self.before
        self.num_of_data -= 1

        return rdata

    def set_sort_rule(self, comp):
        self.comp = comp

    def l_count(self):
        return self.num_of_data