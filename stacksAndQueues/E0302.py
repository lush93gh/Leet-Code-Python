from collections import deque

class E0302:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.dequeue = deque()


    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if not self.dequeue or x <= self.dequeue[-1]:
            self.dequeue.append(x)
        else:
            self.dequeue.appendleft(x)


    def pop(self) -> None:
        if self.stack:
            e = self.stack.pop()
            if self.dequeue[0] == e:
                self.dequeue.popleft()
            else:
                self.dequeue.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else: 
            return -1


    def getMin(self) -> int:
        return self.dequeue[-1]