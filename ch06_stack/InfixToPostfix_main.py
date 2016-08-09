from ch06_stack.InfixToPostfix import conv_to_postfix

exp1 = "1+2*3"
exp2 = "(1+2)*3"
exp3 = "((1-2)+3)*(5-2)"

exp1 = conv_to_postfix(exp1)
exp2 = conv_to_postfix(exp2)
exp3 = conv_to_postfix(exp3)

print(exp1)
print(exp2)
print(exp3)