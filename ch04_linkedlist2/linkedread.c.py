class Node():
    data = None
    next = None

if __name__ == '__main__':
    head = None
    tail = None
    cur = None

    while True:
        read_data = int(input("데이터를 입력하세요."))

        if read_data <= 0:
            break

        new_node = Node()
        new_node.data = read_data
        new_node.next = None

        if head is None:
            # head = new_node
            tail = new_node
        else:
            new_node.next = head
            # tail.next = new_node

        head = new_node
        # tail = new_node

    print("\n 저장된 데이터들을 출력합니다.")

    if head is None:
        print("출력할 데이터가 없습니다")
    else:
        cur = head
        print(cur.data)

        while cur.next is not None:
            cur = cur.next
            print(cur.data)

    print("\n 지금부터 삭제를 시작합니다.")

    if head is None:
        print("삭제할 데이터가 없습니다.")
    else:
        del_node = head
        del_next_node = head.next

        print(id(del_node))
        print(id(head))
        # 실제로 삭제가 안됨. Python에서는 C의 malloc 역할을 하는 함수가 없나봐
        # 밑에서 다시 출력해보면 출력이 안되야 정상인데, 쭉 출력됨.
        del del_node

        while del_next_node is not None:
           del_node = del_next_node
           del_next_node = del_next_node.next

           del del_node

    print("\n 저장된 데이터들을 출력합니다.")

    if head is None:
        print("출력할 데이터가 없습니다")
    else:
        cur = head
        print(cur.data)

        while cur.next is not None:
            cur = cur.next
            print(cur.data)