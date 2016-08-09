from ch07_queue.deque_base_queue import DequeBaseQueue

queue = DequeBaseQueue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

while not queue.is_empty():
    print(queue.q_peek())
    queue.dequeue()