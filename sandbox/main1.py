from sandbox.array_list1 import ArrayList1

al = ArrayList1()

al.l_insert(2)
al.l_insert(4)
al.l_insert(6)
al.l_insert(8)


first = al.l_first()
if first is not None:
    print(first.data)

    next = al.l_next()
    while next is not None:
        print(next.data)
        next = al.l_next()


print("조회 완료. 현재 데이터 수 : {0} \n".format(al.num_of_data))

remove_target = 8


first = al.l_first()
if first is not None:
    if first.data == remove_target:
        print("타겟 발견.")
        al.l_remove()
        print(al.head.data)

    next = al.l_next()
    while next is not None:
        if next.data == remove_target:
            al.l_remove()
        next = al.l_next()

print("삭제 완료. 현재 데이터 수 : {0} \n".format(al.num_of_data))


first = al.l_first()
if first is not None:
    print(first.data)

    next = al.l_next()
    while next is not None:
        print(next.data)
        next = al.l_next()

print("조회 완료. 현재 데이터 수 : {0} \n".format(al.num_of_data))