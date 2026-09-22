class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        #insert val onto stack
        self.stack.append(val)

        #check if minStack is empty or not
        if not self.minStack:
            # insert val onto minStack
            self.minStack.append(val)
        else:
            #find minVal 
            minVal = min(self.minStack[-1], val)
            #insert minVal onto minStack
            self.minStack.append(minVal)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]

   
        
