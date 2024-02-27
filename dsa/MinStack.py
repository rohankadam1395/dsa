class MinStack(object):

    def __init__(self):
        self.stack= []
        self.min = []
        self.minimum = None
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.minimum is None:
            self.minimum = val
        elif val <= self.minimum:
            self.minimum = val
        
        self.min.append(self.minimum)

        

    def pop(self):
        """
        :rtype: None
        """
        self.min.pop()
        if len(self.min) > 0:
            self.minimum = self.min[-1]
        else:
            self.minimum = None
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]

      

# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
# [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647?,null,-2147483648,-2147483648,null,2147483647]
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)

print(obj.top())
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
obj.push(2147483647)
print(obj.top())
print(obj.getMin())
obj.push(-2147483648)
print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.getMin())

