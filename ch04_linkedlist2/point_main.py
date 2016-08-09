from ch04_linkedlist2.dummy_linkedlist import DLinkedList as ArrayList
from ch03_linkedlist1.point import Point

# x좌표 값을 기준, 오름차순 정렬되게
# x좌표 같으면, y 좌표를 대상으로 오름차순 정렬되게.

def point_sorting(d1, d2):
    if d1.xpos < d2.xpos:
        return 0
    elif d1.xpos == d2.xpos:
        if d1.ypos < d2.ypos:
            return 0
        else:
            return 1
    else:
        return 1


al = ArrayList()
al.set_sort_rule(point_sorting)

p = Point(2, 1)
al.l_insert(p)

p = Point(2, 2)
al.l_insert(p)

p = Point(3, 1)
al.l_insert(p)

p = Point(3, 2)
al.l_insert(p)

print("삽입 완료, 데이터 수:{0} \n".format(al.l_count()))

first = al.l_first()
if first:
    first.show_point_pos()

    next = al.l_next()
    while next:
        next.show_point_pos()
        next = al.l_next()

print("조회 완료. \n")
p2 = Point(2, 0)

first = al.l_first()
if first:
    if first.point_comp(p2) == 1:
        al.l_remove()

    next = al.l_next()
    while next:
        if next.point_comp(p2) == 1:
            al.l_remove()

        next = al.l_next()

print("삭제 완료. 데이터 수:{0} \n".format(al.num_of_data))

first = al.l_first()
if first:
    first.show_point_pos()

    next = al.l_next()
    while next:
        next.show_point_pos()
        next = al.l_next()

print("조회 완료.")