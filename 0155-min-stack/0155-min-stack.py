class MinStack(object):

    def __init__(self):
        self.arr = []
        self.minStack = []
        self.minVal = float('inf')
        
    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.arr.append(value)
        
        if self.minStack:
            curr_min = min(self.minStack[-1], value)
        else:
            curr_min = value
        
        self.minStack.append(curr_min)
        

    def pop(self):
        """
        :rtype: None
        """
        self.arr.pop()
        self.minStack.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        
        return self.arr[-1] if self.arr else None
        

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.minStack[-1]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()