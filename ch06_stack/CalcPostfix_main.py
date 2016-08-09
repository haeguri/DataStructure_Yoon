from ch06_stack.CalcPostfix import eval_postfix

# postfix1 = '123*+'
# postfix2 = '12+3*'
# postfix3 = '12-3+52-*'
postfix1 = '42*8+'
postfix2 = '123+*4/'

print(eval_postfix(postfix1))
print(eval_postfix(postfix2))