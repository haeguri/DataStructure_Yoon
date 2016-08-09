STACK_LEN = 100

class StackBasedArray():
    arr = [0 for _ in range(STACK_LEN)]
    top = None

    def __init__(self):
        self.top = -1

    def SPush(self, data):
        if self.top == STACK_LEN-1:
            print("들어갈 자리가 없습니다.")

        self.top += 1
        self.arr[self.top] = data

    def SPop(self):
        if self.SIsEmpty():
            print("뺄 데이터가 없습니다.")
            return None

        rdata = self.arr[self.top]
        self.top -= 1

        return rdata

    def SPeek(self):
        if self.SIsEmpty():
            print("참조할 데이터가 없습니다.")
            return None

        return self.arr[self.top]

    def SIsEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
