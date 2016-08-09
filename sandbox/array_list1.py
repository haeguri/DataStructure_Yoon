"""
더미노드를 사용안한 단방향 연결리스트.
"""

from ch04_linkedlist2.node import Node
import ctypes

class ArrayList1():
    head = None
    cur = None
    before = None
    num_of_data = None

    def __init__(self):
        self.num_of_data = 0

    def l_insert(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        self.num_of_data += 1

    def l_first(self):
        if self.head is None:
            print("조회할 노드가 없습니다.")
            return None

        # 결국 더미 노드를 만들어야함..
        self.before = Node(None)
        self.cur = self.head

        return self.cur

    def l_next(self):
        if self.cur is None:
            print("조회할 노드가 없습니다.")
            return None

        self.before = self.cur
        self.cur = self.cur.next

        return self.cur

    def l_remove(self):
        if self.head is None:
            print("삭제할 노드가 없습니다.")
            return None

        self.before.next = self.cur.next
        del self.cur

        self.cur = self.before
        self.num_of_data -= 1

    def l_count(self):
        pass
