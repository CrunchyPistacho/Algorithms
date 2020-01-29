class Stack:

    def __init__(self):
        self.__stack = []

    def is_empty(self):
        if len(self.__stack) == 0:
            return(0)

    def is_full(self):
        if len(self.__stack) != 0:
            return(len(self.__stack))

    def push(self, value):
        if self.is_full():
            raise IndexError("Stack is full - Overflow Error")
        else:
            self.__stack.append(value)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty - Underflow Error")
        else:
            self.__stack.pop()

    