from collections import deque


class Mystack(object):
    def __init__(self) -> None:
        self.deque_in = deque()
        self.deque_out = deque()

    def push(self, val: int) -> None:
        self.deque_in.append(val)

    def pop(self) -> int:
        if self.empty():
            return None
        return self.deque_in.pop()

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue_in[-1]

    def empty(self) -> bool:
        return len(self.queue_in) == 0
