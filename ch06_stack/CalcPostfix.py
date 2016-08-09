from ch06_stack.BasedArray import StackBasedArray as Stack

def eval_postfix(exp):
    stack = Stack()

    for tok in exp:
        if tok.isdigit():
            stack.SPush(tok)
        elif tok == '+' or tok == '-' or tok == '*' or tok == '/':
            op2 = stack.SPop()
            op1 = stack.SPop()

            e_val = str(eval(op1 + tok + op2))
            stack.SPush(e_val)

    return stack.SPop()