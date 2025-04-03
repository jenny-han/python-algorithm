class MyQueue:

    def __init__(self):
    # 스택을 생성한다.
    # 하나는 메인 스택, 하나는 임시 스택이다.
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:
        if len(self.stack1) == 0 :
            self.stack1.append(x)
        else : 
            while self.stack1 :
                self.stack2.push(self.stack1.pop()) # 기존꺼 옮겨

            self.stack1.append(x) # 새로운 거 넣어

            while self.stack2 :
                self.stack1.push(self.stack2.pop()) # 그 위에 다시 기존꺼 올려 

    def pop(self) -> int:
        if len(self.stack1) > 0 :
            return self.stack1.pop()
        else : 
            print("error")

    def peek(self) -> int:
        if not self.stack1 :
            print("error")
            return None
      
        front = self.stack1.pop() # 맨위의 값을 변수에 넣기
        self.stack1.append(front) # 방금 그 변수 다시 메인 스택에 넣어
        return front # 값 반환
        

    def empty(self) -> bool:
        return len(self.stack1) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



## 개선한 코드
class MyQueue2:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack1) == 0 :
            self.stack1.append(x)
        else : 
            while self.stack1 :
                self.stack2.append(self.stack1.pop())
            self.stack1.append(x) 
            while self.stack2 :
                self.stack1.append(self.stack2.pop()) 

    def pop(self) -> int:
        if not self.stack1 :
            raise IndexError("Queue is empty")
        return self.stack1.pop()

    def peek(self) -> int:
        if len(self.stack1) > 0 :
            self.stack2.append(self.stack1.pop())
            front = self.stack2.pop()
            self.stack1.append(front)
            return front
        else :
            print("error")

    def empty(self) -> bool:
        return not self.stack1

## 방법 2
class MyQueue3:

    def __init__(self):
        self.stack1 = []  # push()를 위한 스택
        self.stack2 = []  # pop()과 peek()을 위한 스택

    def push(self, x: int) -> None:
        """ 큐의 끝에 요소 추가 (O(1)) """
        self.stack1.append(x)

    def pop(self) -> int:
        """ 큐의 앞에서 요소 제거하고 반환 (Amortized O(1)) """
        if not self.stack2:  # stack2가 비었을 때만 stack1 → stack2로 이동
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None  # stack2에서 pop()

    def peek(self) -> int:
        """ 큐의 앞 요소 반환 (삭제 X) (Amortized O(1)) """
        if not self.stack2:  
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] if self.stack2 else None  # stack2의 top 값 반환

    def empty(self) -> bool:
        """ 큐가 비었는지 확인 (O(1)) """
        return not self.stack1 and not self.stack2
