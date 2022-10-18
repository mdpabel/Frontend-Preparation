class Item:
    def __init__(self, val):
        self.val = val
        self.max = None
        self.min = None
        
class MinMaxStack:
    def __init__(self):
        self.stack = []
        
    def top(self):
        n = len(self.stack) 
        if n == 0:
            return
        return self.stack[n - 1]
        
    def peek(self):
        return self.top().val

    def pop(self):
        return self.stack.pop().val

    def push(self, number):
        item = Item(number)
        if len(self.stack) == 0:
            item.max = number
            item.min = number
        else:
            top = self.top()
            item.max = max(top.max, number)
            item.min = min(top.min, number)
        self.stack.append(item)
            

    def getMin(self):
        return self.top().min

    def getMax(self):
        return self.top().max
