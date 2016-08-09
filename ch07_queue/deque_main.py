from ch07_queue.deque import Deque

deque = Deque()

deque.dq_add_first(2)
deque.dq_add_first(1)
deque.dq_add_last(3)
deque.dq_add_last(4)

while not deque.dq_is_empty():
    # print(deque.dq_remove_first())
    # print(deque.dq_remove_last())

    # print(deque.dq_get_first())
    # deque.dq_remove_first()

    print(deque.dq_get_last(), end=" ")
    deque.dq_remove_last()

print()


deque.dq_add_first(2)
deque.dq_add_first(1)
deque.dq_add_last(3)
deque.dq_add_last(4)

while not deque.dq_is_empty():
    # print(deque.dq_remove_first())
    # print(deque.dq_remove_last())

    # print(deque.dq_get_first())
    # deque.dq_remove_first()

    print(deque.dq_get_first(), end=" ")
    deque.dq_remove_first()

