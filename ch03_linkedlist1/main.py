from ch03_linkedlist1.arraylist import ArrayList
from ch03_linkedlist1.point import Point
from ch03_linkedlist1.name_card import NameCard
# from .arraylist import ArrayList

if __name__ == "__main__":
    al = ArrayList()

    nc = NameCard("임꺽정", "010-1111-1111")
    al.l_insert(nc)

    nc = NameCard("홍길동", "010-2222-2222")
    al.l_insert(nc)

    nc = NameCard("변사또", "010-3333-3333")
    al.l_insert(nc)

    first = al.l_first()
    if first:
        if first.name == "변사또":
            first.show_name_card_info()

        next = al.l_next()
        while next:
            if next.name == "변사또":
                next.show_name_card_info()
            next = al.l_next()

    first = al.l_first()
    if first:
        if first.name == "변사또":
            first.change_phone_num("010-3335-3335")

        next = al.l_next()
        while next:
            if next.name == "변사또":
                next.change_phone_num("010-3335-3335")
            next = al.l_next()

    first = al.l_first()
    if first:
        if first.name == "홍길동":
            al.l_remove()

        next = al.l_next()
        while next:
            if next.name == "홍길동":
                al.l_remove()
            next = al.l_next()

    print("남아있는 것들..")

    first = al.l_first()
    if first:
        first.show_name_card_info()

        next = al.l_next()
        while next:
            next.show_name_card_info()
            next = al.l_next()

    print(al.num_of_data)
    print(al.cur_position)


    # point test..
    # al = ArrayList()
    #
    # p = Point(2, 1)
    # al.l_insert(p)
    #
    # p = Point(2, 2)
    # al.l_insert(p)
    #
    # p = Point(3, 1)
    # al.l_insert(p)
    #
    # p = Point(3, 2)
    # al.l_insert(p)
    #
    # print("현재 데이터의 수 : {0} \n".format(al.l_count()))
    #
    # # al.l_insert(11)
    # # al.l_insert(11)
    # # al.l_insert(22)
    # # al.l_insert(44)
    # # al.l_insert(33)
    #
    # first = al.l_first()
    # if first:
    #     first.show_point_pos()
    #
    #     next = al.l_next()
    #     while next:
    #         next.show_point_pos()
    #         next = al.l_next()
    #
    # print()
    #
    # p2 = Point(2, 0)
    #
    # first = al.l_first()
    # if first:
    #     if first.point_comp(p2) == 1:
    #         al.l_remove()
    #
    #     next = al.l_next()
    #     while next:
    #         if next.point_comp(p2) == 1:
    #             al.l_remove()
    #
    #         next = al.l_next()
    #
    # print()
    #
    # print("2. 현재 데이터의 수 : {0}".format(al.num_of_data))
    #
    # first = al.l_first()
    # if first:
    #     first.show_point_pos()
    #
    #     next = al.l_next()
    #     while next:
    #         next.show_point_pos()
    #         next = al.l_next()