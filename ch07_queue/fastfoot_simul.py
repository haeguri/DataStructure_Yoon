import random
from ch07_queue.circle_queue import CircleQueue as Queue, QUEUE_LEN

CUS_COM_TERM = 15

BUL_ID = 0
CHE_ID = 1
DUB_ID = 2

BUL_TERM = 12
CHE_TERM = 15
DUB_TERM = 24

bul_num = 0
che_num = 0
dub_num = 0

waitroom = Queue()
make_proc = 0

for sec in range(1, 3601):
    order_menu = random.randrange(0, 3)

    if sec % CUS_COM_TERM == 0:
        if order_menu == BUL_ID:
            if not waitroom.enqueue(BUL_TERM):
                print("대기실이 꽉 찼습니다. 프로그램이 종료됩니다.")
                break

            bul_num += 1
        elif order_menu == CHE_ID:
            if not waitroom.enqueue(CHE_TERM):
                print("대기실이 꽉 찼습니다. 프로그램이 종료됩니다.")
                break

            che_num += 1
        else:
            if not waitroom.enqueue(DUB_TERM):
                print("대기실이 꽉 찼습니R다. 프로그램이 종료됩니다.")
                break

            dub_num += 1

    if make_proc <= 0 and not waitroom.q_is_empty():
        make_proc = waitroom.dequeue()

    make_proc -= 1

print("대기실 사이즈는..", QUEUE_LEN)
print("불고기버거 개수는..", bul_num)
print("치즈버거 개수는..", che_num)
print("더블버거 개수는..", dub_num)