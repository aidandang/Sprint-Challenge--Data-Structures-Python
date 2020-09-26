class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.tail = 0

    def append(self, item):
        if self.tail < self.capacity:
            self.queue[self.tail] = item
            self.tail += 1
        else:
            self.tail = self.tail % self.capacity
            self.queue[self.tail] = item
            self.tail += 1
    
    def get(self):
        queue = [q for q in self.queue if q is not None]
        return queue