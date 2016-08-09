from ch05_linkedlist3.double_linkedlist import DoubleLinkedList

dll = DoubleLinkedList()

dll.LInsert(2)
dll.LInsert(4)
dll.LInsert(6)
dll.LInsert(8)
dll.LInsert(6)

first = dll.LFirst()
if first is not None:
    print(first.data)

    next = dll.LNext()
    while next is not None:
        print(next.data)
        next = dll.LNext()

print("조회완료! 데이터 개수는 ", dll.num_of_data)

first = dll.LFirst()
if first is not None:
    if first.data == 6:
        dll.LRemove()

    next = dll.LNext()
    while next is not None:
        if next.data == 6:
            dll.LRemove()
        next = dll.LNext()

print("삭제 완료!")


first = dll.LFirst()
if first is not None:
    print(first.data)

    next = dll.LNext()
    while next is not None:
        print(next.data)
        next = dll.LNext()

print("조회완료! 데이터 개수는 ", dll.num_of_data)