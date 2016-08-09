from ch05_linkedlist3.dcircle_linkedlist import DCircleLinkedList

circle_ll = DCircleLinkedList()

circle_ll.LInsertFront(2)
circle_ll.LInsertFront(4)
circle_ll.LInsertFront(6)
circle_ll.LInsertFront(8)

first = circle_ll.LFirst()
if first is not None:
    print(first.data)

    next = circle_ll.LNext()
    for i in range(circle_ll.num_of_data-1):
        print(next.data)
        next = circle_ll.LNext()

print("조회 완료! 데이터개수는 ", circle_ll.LCount())

first = circle_ll.LFirst()
if first is not None:
    if first.data == 8:
        circle_ll.LRemove()

    next = circle_ll.LNext()
    for i in range(circle_ll.num_of_data-1):
        if next.data == 8:
            circle_ll.LRemove()
        next = circle_ll.LNext()

print("삭제 완료 !")

first = circle_ll.LFirst()
if first is not None:
    print(first.data)

    next = circle_ll.LNext()
    for i in range(circle_ll.num_of_data-1):
        print(next.data)
        next = circle_ll.LNext()

print("조회 완료! 데이터개수는 ", circle_ll.LCount())

