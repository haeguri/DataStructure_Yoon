from ch07_queue.circle_queue import CircleQueue as Queue

queue = Queue()

queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
queue.enqueue('D')

# 2, 4, 6

queue.dequeue()
queue.dequeue()
queue.dequeue()

while not queue.q_is_empty():
    print(queue.dequeue())

queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('D')

while not queue.q_is_empty():
    print(queue.dequeue())