class stack:

    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []

    def isEmpty(self):

        if self.list == []:
            return True
        else:
            return False

    def isFull(self):

        if len(self.list) == self.maxSize:
            return 'Stack is full.'

    def push(self,value):

        if self.isFull() == 'Stack is full':
            print('Ab nahi ghus sakta')
        else:
            self.list.append(value)
            return 'element has been pushed'

    ## pop method
    def pop(self):
        if self.isEmpty():
            return 'There is no element in the stack.'
        else:
            print(len(self.list))
            return self.list.pop()

    ## peek
    def peek(self):

        if self.isEmpty():
            return 'There is no element in the stack.'
        else:
            print('Last variable is',self.list[len(self.list)-1])
            return self.list[len(self.list)-1]

    ## delete
    def delete(self):
        self.list = None
    

if __name__ == "__main__":

    a = stack(4)
    a.push(1)
    a.push(2)
    a.push(3)
    print(a.isEmpty())

