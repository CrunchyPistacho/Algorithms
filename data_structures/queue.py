class Queue:

    def __init__(self, Size = 5):
            self.__size = Size
            self.__queue = [None]*Size
            self.__head = self.__tail = 0
            self.__i = -1

    def isEmpty(self):
        if self.__tail == self.__head:
            return(True)

    def isFull(self):
        if self.__tail == self.__size:
            return(True)

    def enqueue(self,value):
        if self.isFull():
            raise IndexError("Queue is Full - Overflow Error")
        else:
            self.__queue[self.__tail] = value
            self.__tail += 1
    

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is Empty - Underflow Error")
        else:
            self.__head +=1
            return(self.__queue[self.__head -1])
