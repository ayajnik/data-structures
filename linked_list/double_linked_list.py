## this code represents double linked list where the node has the capability to move to the next node as well as previous node

class Node:
    '''
    this class will create the value of the node and 
    also the reference of the node to it's next and previous node.
    We will also create a __str__ method to call the value of the newely created node.
    '''
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)
    
class DLL:
    '''
    this class will create the double linked list and will contain
    all the operation that are in-built and can be performed with this data structure.
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

    def __str__(self):
        tempnode = self.head
        result = ''
        while tempnode is not None:
            result += str(tempnode.value)
            if tempnode.next is not None:
                result += ' <-> '
            tempnode = tempnode.next
        return result
    
    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node=Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode)
            currentnode = currentnode.next
    
    def reverse(self):
        currentnode = self.tail
        while currentnode is not None:
            print(currentnode)
            currentnode = currentnode.prev

    def search(self,target):
        currentnode = self.head
        while currentnode is not None:
            if currentnode == target:
                return True
            currentnode = currentnode.next
        return False
    
    def get(self,index):
        
        if index < 0 or index > self.length:
            return False
        if index < self.length//2:
            currentnode = self.head
            for _ in range(index):
                currentnode = currentnode.next
        if index > self.length//2:
            currentnode = self.tail
            for _ in range(index):
                currentnode = currentnode.prev
        return currentnode
    
    def set(self,index,value):
        node = self.get(index)
        if node:
            node.value = value
        else:
        
            return False
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
    
    def pop(self):
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.next = None
        self.length -= 1
    
    def remove(self,index):
        if self.length == 1:
            self.tail = self.head = None
        if index < 0 or self.length < index:
            return False
        else:
            popped_node = self.get(index)
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node = None
        self.length -= 1


if __name__ == '__main__':
    a = DLL()
    a.append(1)
    a.append(3)
    a.append(5)
    a.append(7)
    a.append(9)
    a.prepend(0)
    print(a)

        