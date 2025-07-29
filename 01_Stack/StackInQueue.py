import queue

s = queue.LifoQueue(maxsize=100)

msg = input("문자열 입력: ")
for c in msg:
    s.put(c)    # append랑 같음
    
print("문자열 출력: ", end='')
while not s.empty():
    print(s.get(), end='')
    
# StackInPython 에서 리스트를 LifoQueue 로 구현