# _*_coding:utf-8_*_
# created by Amuu on 2022/9/5

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append((element))

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())

