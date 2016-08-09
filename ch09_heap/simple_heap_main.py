from ch09_heap.simple_heap import Heap

def test_cmp(c1, c2):
    return len(c2) - len(c1)
    # return len(c1) - len(c2)
    # return ord(c2) - ord(c1)


heap_instance = Heap(test_cmp)
heap_instance.h_insert('A')
heap_instance.h_insert('BB')
heap_instance.h_insert('CCC')
heap_instance.h_insert('A')
heap_instance.h_insert('BB')
heap_instance.h_insert('CCC')

# print("left_child of 1" ,heap_instance.get_left_child_pos(1))

# for elem in heap_instance.heap:
#     print( elem )

# print(heap_instance.num_of_data)

while not heap_instance.h_is_empty():
    print(heap_instance.h_delete())