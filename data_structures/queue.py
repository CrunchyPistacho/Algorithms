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


    def __len__(self):
        return(self.__tail - self.__head)


    def __getitem__(self, index):
        if(self.__head <= (index + self.__head) < self.__tail):
            return(self.__queue[index + self.__head])
        else:
            raise IndexError("Index out of range")        

    def __next__(self):
        self.__i += 1
        if self.__i < len(self):
            return self.__getitem__(self.__i)
        else:
            raise StopIteration("Nothing Queued")

    def __iter__(self):
        self.__i = -1
        return(self)



if __name__ == '__main__':

    print("Created Queue of size 5")
    Q1 = Queue(15)
    print("EnQueue (Insert) 2")
    Q1.enqueue(2)
    print("EnQueue 4")
    Q1.enqueue(4)
    print("Print Queue")
  
    for i in Q1:
        print(i, end=", ")

    print("Deleted element = ", Q1.dequeue())
    print("Deleted element = ", Q1.dequeue())
    print("Queue empty")
    print("Deleted element = ", Q1.dequeue())	