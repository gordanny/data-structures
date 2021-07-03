class ListStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not len(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]
