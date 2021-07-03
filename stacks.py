from collections import deque
from queue import LifoQueue


class ListStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]


class DequeStack:
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        return not len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]


class LifoQueueStack:
    def __init__(self):
        self.stack = LifoQueue()

    def is_empty(self):
        return self.stack.empty()

    def push(self, item):
        self.stack.put(item)

    def pop(self):
        return self.stack.get()

    def top(self):
        top_item = self.stack.get()
        self.stack.put(top_item)
        return top_item
