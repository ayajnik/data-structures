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
        while current_node is not None:
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

if __name__ == "__main__":
    a = CircularDoublyLinkedList()
    a.append(1)
    a.append(2)
    a.append(3)
    print(a)



if __name__ == "__main__":
    a = CircularDoublyLinkedList()
    a.append(1)
    a.append(2)
    a.append(3)
    print(a)

