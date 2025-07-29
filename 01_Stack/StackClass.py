class ArrayStack:
    # 생성자
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*capacity
        self.top = -1

    def isEmpty(self):
        if self.top == -1:   
            return True
        else :
            return False

    def isFull(self):
        return self.top == self.capacity

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            pass
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else:
            pass
        
    def peek(self):
        if not isEmpty():
            return self.array[self.top]
        else :
            pass
        
    def size(self):
        return self.top+1
    
    # pop 사용 -> 느림
    def clear(self):
        if self.top == -1:
            pass
        else:
            while self.top != -1:
                self.pop()

    # 빠르게
    def adv_clear(self):
        self.array = [None]*self.capacity
        self.top = -1
        
    # display 추가\
    def display(self):
        print(self.pop(), end='')


s = ArrayStack(100)

msg = input("문자열 입력: ")
for c in msg:
    s.push(c)

# end=' '
# 출력 후 마지막에 무엇을 부틸지 정하는 옵션
# 디폴트는 줄바꿈
print("입력한 문자열 출력: ", end='')
while not s.isEmpty():
    print(s.pop(), end='')
print()

statement = input("괄호문자열 입력: ")

def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch in ('(', "[", "{"):
            stack.push(ch)
        elif ch in (")", "]", "}"):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                    (ch == "]" and left != "[") or \
                    (ch == ")" and left != "(") :
                    return False
    return stack.isEmpty()

print(checkBrackets(statement))