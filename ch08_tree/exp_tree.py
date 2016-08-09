from ch06_stack.BasedArray import StackBasedArray
from ch08_tree.binary_tree import Tree

def print_node(node):
    # print(type(node.data), end=" ")
    # if isinstance(node.data, Tree):
    #     print("이상한것", node.data.left.data, end=" ")
    # else:
    print(node.data, end=" ")

class ExpressionTree():

    def make_exp_tree(self, exp):
        stack = StackBasedArray()

        for c in exp:
            if c.isdigit():
                root = int(c)
            else:
                s2 = stack.SPop()
                s1 = stack.SPop()

                if isinstance(s2, Tree):
                    op2 = s2
                else:
                    op2 = Tree(s2)

                if isinstance(s1, Tree):
                    op1 = s1
                else:
                    op1 = Tree(s1)

                root = Tree(c)

                root.make_right_sub_tree(op2)
                root.make_left_sub_tree(op1)

            stack.SPush(root)

        exp_tree = stack.SPop()

        return exp_tree

    def print_prefix(self, root):
        root.preorder_traversal(root, print_node)

    def print_infix(self, root):
        print("(", end=" ")
        root.inorder_traversal(root, print_node)
        print(")", end=" ")

    def print_postfix(self, root):
        root.postorder_traversal(root, print_node)