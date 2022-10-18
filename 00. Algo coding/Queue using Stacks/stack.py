class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        for i in range(len(self.stack1)-1, -1, -1):
            self.stack2.append(self.stack1[i])
        self.stack1 = []
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[len(self.stack2)-1]
        return self.stack1[0]

    def empty(self) -> bool:
        return self.stack2 == [] and self.stack1 == []
