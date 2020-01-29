class Stack:

    def __init__(self, Size = 5):
        self.__size = Size
        self.__stack = []
        self.__i = -1

    def is_empty(self):
        if len(self.__stack) == 0:
            return(0)

    def is_full(self):
        if len(self.__stack) == self.__size:
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
            return(self.__stack.pop())

    def __len__(self):
        return(len(self.__stack))

    def __getitem__(self,index):
        if index < len(self):
            return(self.__stack[index])
        else:
            raise(IndexError("Index out of range"))
    
    def __previous__(self):
        self.__i -= 1
        if self.__i >= len(self):
            return(self.__stack[self.__i])
        else:
            raise StopIteration("First item reached")

    def __next__(self):
        self.__i += 1
        if self.__i < len(self):
            return(self.__stack[self.__i])
        else:
            raise StopIteration("Last item reached")

    def __iter__(self):
        self.__i = -1
        return(self)

    def __str__(self):
        Values = []
        for i in self.__stack:
            Values.append(str(i))

        return ", ".join(Values)


if __name__ == '__main__':

    S1 = Stack(3)

    for i in range(3):
        print("Insert", i, "in stack")
        S1.push(i)

    print("Stack : ", end="")
    for i in S1:
        print(i, end=", ")

    print("Pop, popped element = ", S1.pop())

    print("Stack :", S1)
