class RingBuffer:
    def __init__(self, capacity = 10):  # 생성자
        self.capacity = capacity        # 크기
        self.array = [None]*capacity    # 큐 배열
        self.front = 0                  # 전단 인덱스
        self.rear = 0                   # 후단 인덱스
        

    # 전단 == 후단 -> 공백 상태
    def isEmpty(self):
        return self.front == self.rear

    # front가 rear의 바로 앞에 있으면 포화
    # 자리 하나를 비워두고 원형큐 설계함
    # 안그러면 공백인 상태와 구분이 안됨
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    # 삽입
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            pass    # Overflow 처리안해요
        
    # 삭제
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            pass    # Underflow 처리안해요
        
    # 맨 앞 요소 들여다보기
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            pass    # Underflow 처리안해요
        
    # 전체 요소의 수 구하기
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    # 전체 요소 출력하기
    def display(self, msg):
        print(msg, end=': [ ')
        for  i in range((self.rear - self.front + self.capacity) % self.capacity):
            print(self.array[(self.front+1+i) % self.capacity], end=' ')
        print(']')
        
    # 링 버퍼 enqueue
    def enqueue2(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            
            
import random

q = RingBuffer(8)

q.display("초기상태")
for i in range(6):
    q.enqueue2(i)
q.display("삽입 0-5")

q.enqueue2(6)
q.enqueue2(7)
q.display("삽입 6, 7")

q.enqueue2(8)
q.enqueue2(9)
q.display("삽입 8, 9")

q.dequeue()
q.dequeue()
q.display("삭제  x2")