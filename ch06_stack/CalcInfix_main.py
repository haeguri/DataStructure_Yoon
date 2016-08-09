from ch06_stack.InfixToPostfix import conv_to_postfix
from ch06_stack.CalcPostfix import eval_postfix

def calc_infix(exp):
    postfix_exp = conv_to_postfix(exp)
    result = eval_postfix(postfix_exp)

    return result

print(calc_infix('1+2*3'))
print(calc_infix('(1+2)*3'))
print(calc_infix('((1-2)+3)*(5-2)'))