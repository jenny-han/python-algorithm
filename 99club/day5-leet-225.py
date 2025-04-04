class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1  :
            self.queue2.append(self.queue1.pop(0))
        top = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, []
        return top

    def top(self) -> int:
        while len(self.queue1) > 1 :
            self.queue2.append(self.queue1.pop(0)) # python에서 큐는 pop(0)를 하면 된다. 
        front = self.queue1[0]
        self.queue2.append(front)
        self.queue1, self.queue2 = self.queue2, [] 
        return front
        
    def empty(self) -> bool:
        return not self.queue1 and not self.queue2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()