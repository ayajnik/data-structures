class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = next


class SLL:
    def __init__(self):
        self.head = None

class stack:
    def __init__(self):
        self.linkedlist = SLL()

    def isEmpty(self):

        if self.linkedlist.head is None:
            return True
        else:
            return False

    def push(self, value):

        node = Node(value)
        node.next = self.linkedlist.head
        self.linkedlist.head = node

    def pop(self):

        if self.isEmpty():
            return 'No element in the stack'

        else:
             nodeValue = self.linkedlist.head.value
             self.linkedlist.hed = self.linkedlist.head.next
             print('Value removed', nodeValue)
             return nodeValue

    def peek(self):

        if self.isEmpty():
            return 'No element in the stack'

        else:
             nodeValue = self.linkedlist.head.value
             
             print('Last value:', nodeValue)
             return nodeValue

    def delete(self):
        self.linkedlist.head = None
        print('Stacked LL deleted')
        return 'Done'


if __name__ == "__main__":

    a = stack()
    a.push(1)
    a.push(2)
    a.push(3)
    a.pop()
    a.peek()
    print(a.isEmpty())
    print(a.delete())
