class E0301:

    def __init__(self, stackSize: int):
        self.stackSize = stackSize
        self.stacks = [-1] * stackSize * 3
        self.top0 = -1
        self.top1 = stackSize * 1 - 1
        self.top2 = stackSize * 2 - 1
        self.tops = {0: self.top0, 1: self.top1, 2: self.top2}

    def push(self, stackNum: int, value: int) -> None:
        if not self.isFull(stackNum):
            self.tops[stackNum] += 1
            top = self.tops.get(stackNum, self.top0)
            self.stacks[top] = value


    def pop(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            top = self.tops.get(stackNum, self.top0)
            self.tops[stackNum] -= 1
            return self.stacks[top]
        else:
            return -1

    def peek(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            top = self.tops.get(stackNum, self.top0)
            return self.stacks[top]
        else:
            return -1

    def isEmpty(self, stackNum: int) -> bool:
        top = self.tops.get(stackNum, self.top0)
        return top == stackNum * self.stackSize  - 1

    def isFull(self, stackNum: int) -> bool:
        top = self.tops.get(stackNum, self.top0)
        return top >= stackNum * self.stackSize + self.stackSize - 1
    