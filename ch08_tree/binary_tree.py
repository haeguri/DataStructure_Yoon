# class Node():
#
#
#     def set_data(self, data):
#         self.data = data
#
class Tree():
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def make_left_sub_tree(self, sub):
        self.left = sub

    def make_right_sub_tree(self, sub):
        self.right = sub

    def preorder_traversal(self, node, action):
        if node is None:
            return

        action(node)
        node.preorder_traversal(node.left, action)
        node.preorder_traversal(node.right, action)

    def inorder_traversal(self, node, action):
        if node is None:
            return

        node.inorder_traversal(node.left, action)
        action(node)
        node.inorder_traversal(node.right, action)

    def postorder_traversal(self, node, action):
        if node is None:
            return

        node.postorder_traversal(node.left, action)
        node.postorder_traversal(node.right, action)
        action(node)

    # def del_tree(self, node):
    #     if node is None:
    #         return
    #
    #     self.del_tree(node.left)
    #     self.del_tree(node.right)
    #     if node.data == 6:
    #         node.data = None