from ch07_queue.list_base_queue import ListBaseQueue

llq = ListBaseQueue()

llq.enqueue(1)
llq.enqueue(2)
llq.enqueue(3)
llq.enqueue(4)

while not llq.is_empty():
    print(llq.q_peek())
    llq.dequeue()
