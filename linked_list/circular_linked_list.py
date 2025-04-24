class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result


    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self,index,value):
        new_node=Node(value)
        if index < 0 or index > self.length:
            raise Exception("Invalid Index reference")
        if self.length == 0:
            if index == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                new_node = self.head
                self.tail.next = self.head
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
    def traverse(self):
       temp_node = self.head
       while temp_node is not None:
           print(temp_node)
           temp_node = temp_node.next
           if temp_node.next == self.head:
               break 
           
    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self,index):
        if index == -1:
            return self.tail
        elif index < -1 or index > self.length:
            return None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
        
    def set_value(self,index,value):
        val = self.get(index)
        if val:
            val.value = value

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = self.tail = None
        else:
            popped_node = self.head
            self.head = self.head.next
            self.tail.next = self.head
            popped_node = None
        self.length-=1 

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = self.tail = None
        else:
            popped_node = self.tail
            temp = self.head
            while temp.next is not popped_node:
                temp = temp.next
            temp.next = self.head
        popped_node = None
        self.length-=1        

    def remove(self,index):
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node = None
        self.length-=1
    
    def delete_all(self):
        self.tail = None
        self.head = None
        self.length = 0
            
if __name__ == "__main__":
    a = CLL()
    a.append(1)
    a.append(2)
    a.prepend(0)
    a.insert(3,10)
    a.insert(1,10)
    a.insert(2,30)
    a.traverse()
    a.search(10)
    a.set_value(5,90)
    a.pop_first()
    a.pop()
    a.remove(1)
    a.delete_all()
    print(a)