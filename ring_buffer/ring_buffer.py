#import ipdb


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = 0
        self.buffer = []

    def append(self, item):
        # ipdb.set_trace()
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        else:
            self.buffer[self.oldest] = item
        self.oldest = (self.oldest + 1) % self.capacity

    def get(self):
        return [node for node in self.buffer if node is not None]


# Manual testing
# buffer = RingBuffer(3)

# print(buffer.get())   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# print(buffer.get())   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# print(buffer.get())   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# print(buffer.get())   # should return ['d', 'e', 'f']
