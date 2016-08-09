from ch08_tree.exp_tree import ExpressionTree, print_node
from ch06_stack.InfixToPostfix import conv_to_postfix

exp_tree = ExpressionTree()

postfix_exp = conv_to_postfix('(1+2)*7')
# postfix_exp = conv_to_postfix('(1+2)')

print("후위 연산자", postfix_exp)

root = exp_tree.make_exp_tree(postfix_exp)

exp_tree.print_prefix(root)
print()
exp_tree.print_infix(root)
print()
exp_tree.print_postfix(root)

# print()
# print(root.postorder_traversal(root, print_node))