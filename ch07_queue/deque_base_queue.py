from ch07_queue.deque import Deque

class DequeBaseQueue():

    def __init__(self):
        self.queue = Deque()

    def enqueue(self, data):
        self.queue.dq_add_last(data)

    def dequeue(self):
        # if self.queue.dq_is_empty():
        #     print("삭제할 데이터가 없습니다.")
        #     return None

        return self.queue.dq_remove_first()

    def q_peek(self):
        # if self.queue.dq_is_empty():
        #     print("조회할 데이터가 없습니다.")
        #     return None

        return self.queue.dq_get_first()

    def is_empty(self):
        return self.queue.dq_is_empty()
        #     return True
        # else:
        #     return False