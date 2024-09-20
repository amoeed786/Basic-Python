class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
        
    def is_empty(self):
        return self.top == -1
        
    def is_full(self):
        return self.top == self.size - 1
        
    def push(self, data):
        if self.is_full():
            print("Stack is full!")
            return False
        else:
            self.top += 1
            self.stack[self.top] = data
            return True
        
    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        else:
            data = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return data
        
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        else:
            return self.stack[self.top]
        
    def print_stack(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack elements are:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])
    
    def count(self):
        return self.top + 1
