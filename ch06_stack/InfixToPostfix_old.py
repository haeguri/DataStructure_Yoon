from ch06_stack.BasedArray import StackBasedArray as Stack

def get_op_prec(op):
    if op == '*' or op == '/':
        return 5
    elif op == '+' or op == '-':
        return 3
    elif op == '(':
        return 1
    else:
        return -1

def who_prec_op(op1, op2):
    op1_prec = get_op_prec(op1)
    op2_prec = get_op_prec(op2)

    if op1_prec > op2_prec:
        return 1
    elif op1_prec < op2_prec:
        return -1
    else:
        return 0

def conv_to_rpn_exp(exp):
    stack = Stack()
    conv_exp = ''

    for tok in exp:
        if tok.isdigit():
            conv_exp += tok
        else:
            if tok == '(':
                stack.SPush(tok)
            elif tok == ')':
                while True:
                    pop_op = stack.SPop()
                    if pop_op == '(':
                        break
                    conv_exp += pop_op
            elif tok == '+' or tok == '-' or tok == '*' or tok == '/':
                while not stack.SIsEmpty() and who_prec_op(stack.SPeek(), tok) >= 0:
                    conv_exp += stack.SPop()

                stack.SPush(tok)
            else:
                pass

    while not stack.SIsEmpty():
        conv_exp += stack.SPop()

    exp = conv_exp
    del conv_exp

    return exp