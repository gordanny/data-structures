from collections import deque
from queue import Queue
from multiprocessing import Queue as MultiprocessingQueue


class ListQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return not len(self.queue)

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)


class DequeQueue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return not len(self.queue)

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.popleft()


class QueueQueue:
    def __init__(self):
        self.queue = Queue()

    def is_empty(self):
        return self.queue.empty()

    def push(self, item):
        self.queue.put_nowait(item)

    def pop(self):
        return self.queue.get_nowait()


class MultiprocessingQueueQueue:
    def __init__(self):
        self.queue = MultiprocessingQueue()

    def is_empty(self):
        return self.queue.empty()

    def push(self, item):
        self.queue.put(item)

    def pop(self):
        return self.queue.get()

