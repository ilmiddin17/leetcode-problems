class MinStack:

    def __init__(self):
        self.array=[]
        

    def push(self, val: int) -> None:
        self.array.append(val)

    def pop(self) -> None:
        if self.array:
            self.array.pop()
        else:
            return 'Stack is already empty'

    def top(self) -> int:
        if self.array:
            return self.array[-1]
        else:
            return 'Stack is empty'

    def getMin(self) -> int:
        if self.array:
            return min(self.array)
        else:
            'Stack is empty'


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
