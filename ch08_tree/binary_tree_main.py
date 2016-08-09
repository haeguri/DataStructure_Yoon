from ch08_tree.binary_tree import Tree

def print_node(node):
    # if node.data is not None:
    #     print(node.data, end=" ")

    print(node.data, end=" ")

def print_node_id(node):
    print("data:{0}, id:{1}".format(node.data, id(node)))

# btree = Tree()

bt1 = Tree(1)
bt2 = Tree(2)
bt3 = Tree(3)
bt4 = Tree(4)
bt5 = Tree(5)
bt6 = Tree(6)

bt1.make_left_sub_tree(bt2)
bt1.make_right_sub_tree(bt3)
bt2.make_left_sub_tree(bt4)
bt2.make_right_sub_tree(bt5)
bt3.make_right_sub_tree(bt6)

bt1.preorder_traversal(bt1, print_node)
print()
bt1.inorder_traversal(bt1, print_node)
print()
bt1.postorder_traversal(bt1, print_node)
print()

# btree.del_tree(bt1)

# btree.inorder_traversal(bt1, print_node)

# bt1.inorder_traversal(bt1, print_node)
# print()