from ch04_linkedlist2.dummy_linkedlist import DLinkedList

def ascending_integer(d1, d2):
    if d1 < d2:
        return 0
    else:
        return 1


dlinkedlist = DLinkedList()

# dlinkedlist.set_sort_rule(ascending_integer)

dlinkedlist.l_insert(8)
dlinkedlist.l_insert(6)
dlinkedlist.l_insert(4)
dlinkedlist.l_insert(2)
dlinkedlist.l_insert(4)
dlinkedlist.l_insert(4)
dlinkedlist.l_insert(4)
dlinkedlist.l_insert(7)
print("삽입 완료\n")

first = dlinkedlist.l_first()
if first is not None:
    print(first)

    next = dlinkedlist.l_next()
    while next is not None:
        print(next)
        next = dlinkedlist.l_next()

print("조회 완료\n")

remove_target = 7

first = dlinkedlist.l_first()
if first is not None:
    if first == remove_target:
        print("{0}가 삭제 됩니다.".format(dlinkedlist.l_remove()))

    next = dlinkedlist.l_next()
    while next is not None:
        if next == remove_target:
            print("{0}가 삭제 됩니다.".format(dlinkedlist.l_remove()))
        next = dlinkedlist.l_next()

print("삭제 완료\n")

first = dlinkedlist.l_first()
if first is not None:
    print(first)

    next = dlinkedlist.l_next()
    while next is not None:
        print(next)
        next = dlinkedlist.l_next()

print("조회 완료")