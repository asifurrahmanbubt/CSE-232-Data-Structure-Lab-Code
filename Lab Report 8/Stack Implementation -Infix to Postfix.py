class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek into an empty stack")

    def size(self):
        return len(self.items)


def is_operator(char):
    return char in "+-*/"


def has_higher_precedence(op1, op2):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    return precedence[op1] >= precedence[op2]


def infix_to_postfix(expression):
    stack = []
    postfix = []
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop the '('
        elif is_operator(char):
            while stack and stack[-1] != '(' and has_higher_precedence(stack[-1], char):
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)


infix_expression = "3 + 5 * ( 2 - 6 ) / 4"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)
