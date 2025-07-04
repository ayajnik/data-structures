## below constructor method is an example of the implementation logic behind circular double linked list and is not the actual constructor
    # def __init__(self,value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     new_node.prev = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
            result += '<->'
        return result

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

        self.length += 1
    
    def prepend(self,value):

        new_node = Node(value)

        if self.length == 0:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1

    def traverse(self):
        if self.head is None:
            return  # or print("List is empty")

        current_node = self.head
        while True:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
    
    def reverse_traverse(self):

        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break
    
    def search(self,target):

        current_node = self.head
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
            if current_node == self.head:
                break
        return False

    def get(self,index):

        current_node = None
        if self.length // 2 < index:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
            print('Node found in first half of LL')
        else:
            current_node = self.tail
            for i in range(self.length-1,index,-1):
                current_node = current_node.prev
            print('Node found in second half of LL')
        return current_node

    def set_value(self,index,value):

        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,value,index):

        if index == 0:
            self.append(value)
        elif index == -1:
            self.prepend(value)
        elif index < 0 or index > self.length:
            raise IndexError
        
        new_node = Node(value)
        temp_node = self.get(index-1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1
    
    def popped_first(self):
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        popped_node.prev = None
        self.head.prev = self.tail
        self.tail.next = self.head
        self.length -= 1

    def pop(self):

        popped_node = self.tail
        self.tail = self.tail.prev
        popped_node.next = None
        popped_node.prev = None
        self.tail.next = self.head
        self.head.prev = self.tail
        self.length -= 1

    def remove(self,index):

        popped_node = self.get(index)
        popped_node.next.prev = popped_node.prev
        popped_node.prev.next = popped_node.next
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1

    def delete_all(self):

        self.head = None
        self.tail = None
        self.length = 0
        print("Complete LL has been deleted")





if __name__ == "__main__":

    a = CircularDoublyLinkedList()
    a.append(0)
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.prepend(-1)
    
    print(a.search(3))
    print(a.get(2))
    print(a.set_value(2,60))
    
    a.insert(70,3)
    
    a.popped_first()
    a.pop()
    a.remove(2)
    a.reverse_traverse()
    a.delete_all()