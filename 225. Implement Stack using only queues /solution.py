import queue
class MyStack:

    def __init__(self):
        self.queue_1 = queue.Queue()
        self.queue_2 = queue.Queue()

    def push(self, x: int) -> None:
        self.queue_1.put(x)

    def pop(self) -> int:
        while self.queue_1.qsize() > 1:
            item = self.queue_1.get()
            self.queue_2.put(item)

        top_item = self.queue_1.get()
        
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1

        return top_item


    def top(self) -> int:
        while self.queue_1.qsize() > 1:
                item = self.queue_1.get()
                self.queue_2.put(item)

        top_item = self.queue_1.get()
        self.queue_2.put(top_item)
            
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1

        return top_item
        
    def empty(self) -> bool:
        return self.queue_1.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
