capacity = 10
array = [None]*capacity # 크기 10의 초기값이 전부 None 인게 capacity개
top = -1

# 공백 상태 검사
def isEmpty():
    if top == -1:   
        return True
    else :
        return False

# 포화 상태 검사
def isFull():
    return top == capacity

# 스택 삽입
def push(e):
    global top
    if not isFull():
        # Python에서는 함수 내부에서 값을 변경 시 해당 변수를 '지역 변수'로 간주
        # global top 이 없으면 top 을 새로 만드는 지역 변수로 착각함. -> 초기화되지 않은 값을 참조
        top += 1
        array[top] = e
    else:
        print("Stack Overflow")
        exit()
        
# 스택 삭제
def pop():
    global top
    if not isEmpty:
        top -= -1
        return array[top+1]
    else:
        print("Stack Underflow")
        exit()
        
# 
def peek():
    if not isEmpty:
        return array[top]
    else:
        pass
    
def size():
    return top+1