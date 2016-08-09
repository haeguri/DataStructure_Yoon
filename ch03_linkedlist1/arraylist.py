from ch03_linkedlist1.point import Point

LIST_LEN = 100
TRUE = 1
FALSE = 0

class ArrayList():
    arr = [None for x in range(LIST_LEN)]

    def __init__(self):
        self.num_of_data = 0
        self.cur_position = -1

    def l_insert(self, data):
        if self.num_of_data >= LIST_LEN:
            # print("저장할 공간이 없습니다.")
            return
        
        self.arr[self.num_of_data] = data
        self.num_of_data += 1

    def l_first(self):
        if self.num_of_data == 0:
            # print("참조할 데이터가 없습니다.")
            return
        
        self.cur_position = 0
        return self.arr[0]

    def l_next(self):
        if self.cur_position >= self.num_of_data - 1 :
            # print("맨 끝 데이터 입니다.")
            return

        self.cur_position += 1
        return self.arr[self.cur_position]

    def l_remove(self):
        if self.num_of_data == 0:
            # print("삭제할 데이터가 없습니다.")
            return

        rpos = self.cur_position
        rdata = self.arr[self.cur_position]

        for i in range(rpos, self.num_of_data-1):
            self.arr[i] = self.arr[i+1]

        self.num_of_data -= 1
        self.cur_position -= 1

        return rdata

    def l_count(self):

        return self.num_of_data