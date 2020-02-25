class Node:

    def __init__(self, Parent = None, Value = None, Left = None, Right = None):
        self.parent = Parent
        self.value = Value
        self.left = Left
        self.right = Right

    def __str__(self):
        return(str(self.value))

class BinarySearchTree:

    def __init__(self):
        self.__root = None

    def is_empty(self):
        return(self.__root == None)

    def maximum(self, current = -1):
        if current == -1:
            current = self.__root

        while current and current.right != None :
            current = current.right
        return(current)

    def minimum(self, current = -1):
        if current == -1:
            current = self.__root

        while current and current.left != None :
            current = current.left
        return(current)

    def replace(self, a, b):
        if a.parent == None:
            self.__root = b
        elif a.parent.left == a:
            a.parent.left = b
        else: 
            a.parent.right = b

        if b != None:
            b.parent = a.parent

    def successor(self, node):
        if node.right == None:
            while node.parent != None and node.parent.right == node:
                node = node.parent
            return(node.parent)
        else:
            return(self.maximum(node.left))

    def predecessor(self, node):
        if node.left == None:
            while node.parent != None and node.parent.left == node :
                node = node.parent
            return(node.parent)
        else:
            return(self.maximum(node.left))


    def insert(self,v):
        if self.is_empty():
            self.__root = Node(Value = v)
        else:
            current = self.__root
            while(current != None):
                parent = current
                if v <= current.value:
                    current = current.left
                else:
                    current = current.right
            if v <= parent.value:
                parent.left = Node(parent,v)
            else:
                parent.right = Node(parent,v)

    def delete(self,node_del):
        if node_del:
            if node_del.left == None:
                self.replace(node_del,node_del.right)      
            elif node_del.right == None:
                self.replace(node_del,node_del.left)
            else:
                tmp = self.successor(node_del)
                if( tmp != node_del.right ):
                    self.replace(tmp, tmp.right)
                    tmp.right = node_del.right
                    tmp.right.parent = tmp
                self.replace(node_del, tmp)
                tmp.left = node_del.left
                tmp.left.parent = tmp
            node_del.parent = node_del.left = node_del.right = None
            return(node_del)
        else:
            return(None)

    def preorder(self, current = -1):
        R = []
        if current == -1:
            current = self.__root
        if current != None:
            R.append(current.value) 
            R.extend(self.preorder(current.left))
            R.extend(self.preorder(current.right))
        return(R)

    def inorder(self, current = -1):
        R = []
        if current == -1 :
            current = self.__root
        if current != None:
            R.extend(self.inorder(current.left))
            R.append(current.value)
            R.extend(self.inorder(current.right))
        return(R)

    def postorder(self, current = -1):
        if current == -1:
            current = self.__root
        R = []
        if(current != None):
            R.extend(self.postorder(current.left))
            R.extend(self.postorder(current.right))
            R.append(current.value)
        return(R)

    def levelorder(self, current = -1):
        R = []
        next_l = []

        if self.is_empty():
             return(R) 
        if current == -1:
            current = [self.__root] 
            R.append(self.__root.value) 
        for each in current: 
            if each.left != None:
                R.append(each.left.value)
                next_l.append(each.left)
            if each.right != None:
                R.append(each.right.value)
                next_l.append(each.right)
        if next_l:
            R.extend(self.levelorder(next_l))
        return(R)

    def search(self, find):
        current = self.__root
        while current and current.value != find : 
            if current.value < find:
                current = current.right
            else:
                current = current.left