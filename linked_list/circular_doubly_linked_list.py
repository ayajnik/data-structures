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


if __name__ == "__main__":

    a = CircularDoublyLinkedList()
    a.append(0)
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.prepend(-1)
    a.reverse_traverse()
    print(a.search(3))