from ch05_linkedlist3.circle_linkedlist import CircleLinkedList


class BasedCLL():
    cll = None

    def __init__(self):
        self.cll = CircleLinkedList()

    def SPush(self, data):
        self.cll.LInsertFront(data)

    def SPop(self):
        if self.SIsEmpty():
            print("꺼낼 데이터가 없습니다.")
            return None

        rdata = self.cll.LFirst().data
        self.cll.LRemove()

        return rdata

    def SPeek(self):
        if self.SIsEmpty():
            print("참조할 데이터가 없습니다.")
            return None

        rdata = self.cll.LFirst().data
        return rdata

        pass

    def SIsEmpty(self):
        if self.cll.LCount() == 0:
            return True
        else:
            return False
