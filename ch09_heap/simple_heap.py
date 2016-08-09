HEAP_LEN = 100

class Heap():
    def __init__(self, comp):
        self.num_of_data = 0
        self.heap = [0 for _ in range(HEAP_LEN)]
        self.comp = comp

    def get_left_child_pos(self, pos):
        return pos * 2

    def get_right_child_pos(self, pos):
        return self.get_left_child_pos(pos) + 1

    def get_parent_pos(self, pos):
        return pos // 2

    def get_hi_pr_chilid(self, pos):
        if self.get_left_child_pos(pos) > self.num_of_data:
            return 0
        elif self.get_left_child_pos(pos) == self.num_of_data:
            return self.get_left_child_pos(pos)
        else:
            if self.comp(self.heap[self.get_left_child_pos(pos)], self.heap[self.get_right_child_pos(pos)]) < 0:
            # 오르쪽의 우선순위가 높다면.. (오른쪽의 아스키코드 값이 더 작다면) ?
                return self.get_right_child_pos(pos)
            else:
                return self.get_left_child_pos(pos)

    def h_insert(self, data):
        helem = data
        idx = self.num_of_data + 1

        while idx != 1:
            # 마지막 자리에 삽입된 데이터보다 부모 노드의 데이터의 우선순위가 더 작다면.
            # 마지막 데이터의 아스키코드값보다 부모 노드의 아스키코드 값이 크다면.
            if self.comp(data, self.heap[self.get_parent_pos(idx)]) >= 0:
                self.heap[idx] = self.heap[self.get_parent_pos(idx)] # 부모의 것을 끌어내리고.
                idx = self.get_parent_pos(idx)
            else:
                break

        self.heap[idx] = helem
        self.num_of_data += 1

    def h_delete(self):
        ret_data = self.heap[1]
        last_elem = self.heap[self.num_of_data]

        parent_idx = 1
        child_idx = self.get_hi_pr_chilid(parent_idx)

        while child_idx:
            # 마지막 자리의 데이터보다 비교 대상의 노드(자식 노드)가 우선순위가 낮다면.
            # 마지막 자리의 데이터가 아스키코드 값이 더 작다면.
            if self.comp(last_elem, self.heap[child_idx]) >= 0:
                break

            self.heap[parent_idx] = self.heap[child_idx]
            parent_idx = child_idx

            child_idx = self.get_hi_pr_chilid(parent_idx)

        self.heap[parent_idx] = last_elem
        self.num_of_data -= 1
        return ret_data

    def h_is_empty(self):
        if self.num_of_data == 0:
            return True
        else:
            return False