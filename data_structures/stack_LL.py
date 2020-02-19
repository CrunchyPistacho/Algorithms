class Node:

     def __init__(self, Value, Next=None):
        self.value = Value      
        self.next = Next         

class Stack_LL:

    def __init__(self):
        self.__top = None
        self.__len = 0
        self.__i = None

    def is_empty(self):
        return(self.__top == None)

    def push(self, value):
        self.__top = Node(value, self.__top)
        self.__len += 1

    def pop(self):
        if(self.is_empty()): raise IndexError("Stack is Empty")
        else:
            tmp = self.__top 
            self.__top = self.__top.next
            tmp.next = None
            self.__len -= 1
            return(tmp.value)

    def __len__(self):
        return(self.__len)

    def __next__(self):
        tmp = self.__i
        if (tmp == None): raise StopIteration("Last item reached")
        self.__i = self.__i.next
        return(tmp.value)
     
    def __iter__(self):
        self.__i = self.__top
        return(self)

    def __str__(self):
        tmp = self.__top
        Values = []
        while tmp:
            Values.append(str(tmp.value))
            tmp = tmp.next
        Values.append("None")
        return(" -> ".join(Values))



if __name__ == '__main__':
    S1 = Stack_LL()

    for i in range(5, 15, 2):
        print("push", i, "to stack")
        S1.push(i)

    print("\nStack : ", S1)

    print("\nPop stack, popped value = ", S1.pop())   