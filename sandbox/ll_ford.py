from ch04_linkedlist2.dummy_linkedlist import DLinkedList as LinkedList



ll = LinkedList()

ll.f_insert('f')
ll.f_insert('e')
ll.f_insert('d')
ll.f_insert('c')
ll.f_insert('b')
ll.f_insert('a')

test = []

first = ll.l_first()
if first is not None:
    test.append(first.data)

    next = ll.l_next()
    while next is not None:
        test.append(next.data)
        next = ll.l_next()

print(test)

s_wall = 0
e_wall = len(test)-1
result = ""

while e_wall >= s_wall:
    if e_wall != s_wall:
        result = result + test[s_wall] + test[e_wall]
    else:
        result = result + test[s_wall]

    e_wall -= 1
    s_wall += 1

print("result is", result)



