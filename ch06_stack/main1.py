# from ch06_stack.BasedArray import StackBasedArray as Stack
from ch06_stack.BasedLinkedList import BasedLinkedList as Stack

stack = Stack()

stack.SPush(2)
stack.SPush(4)
stack.SPush(6)
stack.SPush(8)

while not stack.SIsEmpty():
    print(stack.SPeek())
    stack.SPop()
    # print()