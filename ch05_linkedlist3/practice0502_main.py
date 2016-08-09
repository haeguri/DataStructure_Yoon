from ch05_linkedlist3.circle_linkedlist import CircleLinkedList
from ch05_linkedlist3.employee import Employee

circle_ll = CircleLinkedList()

circle_ll.LInsert(Employee(1234, "가나다"))
circle_ll.LInsert(Employee(2345, "나다라"))
circle_ll.LInsert(Employee(3456, "다라마"))
circle_ll.LInsert(Employee(4567, "라마바"))

first = circle_ll.LFirst()
if first is not None:
    first.data.show_info()

    next = circle_ll.LNext()
    for i in range(circle_ll.num_of_data-1):
        next.data.show_info()
        next = circle_ll.LNext()

print("조회 완료")

target_name = "나다라"
days = 3

cur = circle_ll.LFirst()
if cur is not None:
    for i in range(circle_ll.num_of_data-1):
        if cur.data.name == target_name:
            break
        cur = circle_ll.LNext()
    for i in range(days):
        cur = circle_ll.LNext()

    print("당직자는..")
    cur.data.show_info()