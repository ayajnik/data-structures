class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = None
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length = self.length + 1
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += self.length

    def insert(self,index,value):
        new_node = Node(value)
        temp_node = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length = self.length + 1 
    
    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next        

    def search(self,target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False
    
    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            raise Exception
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node
    
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            raise Exception
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            temp_node.next = None
            self.tail = temp_node
        self.length = self.length - 1
        return popped_node
    
    def remove(self,index):
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length = self.length - 1
        return popped_node
    
    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0
    


if __name__ == "__main__":
    a = SLL()
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    a.prepend(0)
    a.insert(3,10)
    a.search(10)
    a.get(-1)
    a.traverse()
    a.set_value(4,20)
    a.pop_first()
    a.pop()
    a.remove(4)
    a.delete()
    print(a)
