QUEUE_LEN = 30

class CircleQueue():
    arr = [0 for _ in range(QUEUE_LEN)]
    front = None
    rear = None

    def __init__(self):
        self.front = 0
        self.rear = 0

    def get_next_pos(self, pos):
        if pos == QUEUE_LEN-1:
            return 0
        else:
            return pos+1

    def enqueue(self, data):
        next_pos = self.get_next_pos(self.rear)

        if next_pos == self.front:
            print("큐가 꽉 찼습니다.")
            return False

        self.rear = next_pos
        self.arr[next_pos] = data

        return True

    def dequeue(self):
        if self.q_is_empty():
            print("꺼낼 데이터가 없습니다.")
            return None

        self.front = self.get_next_pos(self.front)

        return self.arr[self.front]

    def q_peek(self):
        if self.q_is_empty():
            print("꺼낼 데이터가 없습니다.")
            return None

        return self.arr[self.get_next_pos(self.front)]

    def q_is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False


