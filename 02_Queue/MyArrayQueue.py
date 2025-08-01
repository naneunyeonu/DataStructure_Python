class MyArrayQueue:
    # 생성자
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None]*capacity
        self.front = 0
        self.rear = 0
        
    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            pass
        
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            item = self.array[self.front]
            self.array[self.front] = None
            return item
        else:
            pass

    def peek(self):
        if not isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            pass
        
    def display(self, msg):
        print(msg, end=': [')
        for i in range((self.rear - self.front + self.capacity) % self.capacity):
            print(self.array[(self.front + 1 + i) % self.capacity], end=' ')
        print(']')
            
import random

q = MyArrayQueue(10)

q.display("초기 상태")
while not q.isFull():
    q.enqueue(random.randint(0, 100))
q.display("포화 상태")

q.display("삭제 순서")
while not q.isEmpty():
    print(q.dequeue(), end=' ')
print()