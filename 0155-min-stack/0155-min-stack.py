class MinStack:

    def __init__(self):
        self.arr = []
        self.minStack = []
    def push(self, value: int) -> None:
        self.arr.append(value)

        if self.minStack:
            current_min = min(self.minStack[-1], value)
        else:
            current_min = value
        
        self.minStack.append(current_min)
        

    def pop(self) -> None:
        self.arr.pop()
        self.minStack.pop()

        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()