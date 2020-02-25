class Node:

    def __init__(self, Value=None, Prev=None, Next=None):
        self.value = Value
        self.next = Next
        self.prev = Prev

class Queue_LL:

    def __init__(self):    
        self.__head = Node()
        self.__tail = Node(Prev = self.__head)
        self.__head.next = self.__tail
        self.__len = 0
        self.__i = None

    def is_empty(self):
        if self.__len == 0:
            return(True)

    def enqueue(self, Value):
        tmp = Node(Value, self.__tail.prev, self.__tail)
        self.__tail.prev.next  = tmp
        self.__tail.prev = tmp
        self.__len += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is Empty - Uderflow Error")
        else:
            tmp = self.__head.next
            self.__head.next = tmp.next
            tmp.next.prev = self.__head
            self.__len -= 1
            return(tmp.value)

    def __len__(self):
        return(self.__len)

    def __next__(self):
        if(self.__i != self.__tail):
            self.__i = self.__i.next
            return(self.__i.prev.value)
        else:
            raise StopIteration("Nothing Queued")
    
    def __iter__(self):
        self.__i = self.__head.next
        return(self)

    def __str__(self):
        Values = []
        for i in self:
            Values.append(str(i))
        return(", ".join(Values))


if __name__ == '__main__':

    Q_LL = Queue_LL()

    for i in range(5):
        print("Insert", i)
        Q_LL.enqueue(i)

    print("\nQueue :", end="")
    for i in Q_LL:
        print(i, end=", ")

    print("\n\nDequeue, Deleted value = ", Q_LL.dequeue())

    print("\nDequeue = ", Q_LL)
