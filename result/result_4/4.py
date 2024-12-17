from typing import List
from typing import List
def isOperator(c):
    return c == '+' or c == '-' or c == '*' or c == '/'
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0
def isHigherPrecedence(op1, op2):
    return precedence(op1) > precedence(op2)
def infixToPostfix(infix):
    operators = []
    postfix = ""
    mayBeUnary = True
    i = 0
    while i < len(infix):
        c = infix[i]
        if c.isspace():
            continue
        elif c.isdigit():
            postfix += c
            while i + 1 < len(infix) and infix[i + 1].isdigit():
                i += 1
                postfix += infix[i]
            postfix += " "
            mayBeUnary = False
        elif c == '(':
            operators.append(c)
            mayBeUnary = True
        elif c == ')':
            while not not operators and operators[-1] != '(':
                postfix += operators[-1] + str(" ")
                operators.pop()
            operators.pop()
            mayBeUnary = False
        elif isOperator(c):
            if mayBeUnary and c == '-':
                postfix += "0 "
                operators.append('-')
            else:
                while not not operators and precedence(operators[-1]) >= precedence(c) and operators[-1] != '(':
                    postfix += operators[-1] + str(" ")
                    operators.pop()
                operators.append(c)
            mayBeUnary = True
        i += 1
    while not not operators:
        postfix += operators[-1] + str(" ")
        operators.pop()
    return postfix
def applyOp(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    return 0
def evaluatePostfix(postfix):
    values = []
    i = 0
    while i < len(postfix):
        if postfix[i].isspace():
            i += 1
            continue
        elif postfix[i].isdigit():
            val = 0
            while i < len(postfix) and postfix[i].isdigit():
                fix_tmp = postfix[i]
                tmp_str = fix_tmp
                val = val * 10 + int(tmp_str)
                i += 1
            values.append(val)
        elif isOperator(postfix[i]):
            val2 = values[-1]
            values.pop()
            val1 = values[-1]
            values.pop()
            values.append(applyOp(val1, val2, postfix[i]))
            i += 1
    return values[-1]
def main():
    expression = None
    print("Enter an expression: ", end=' ')
    expression = input()
    postfix = infixToPostfix(expression)
    print("Postfix expression: ", postfix, "\n", end=' ')
    result = evaluatePostfix(postfix)
    print("The result is: ", result, "\n", end=' ')
    return 0


if __name__ == '__main__':
    main()