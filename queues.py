class ListQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return not len(self.queue)

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)
