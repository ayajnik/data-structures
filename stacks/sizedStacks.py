## operations:

## 1. Creation
## 2. Push --> insert
## 3. Pop --> remove
## 4. Peek --> will always return the top most element in the stack
## 5. isEmpty --> to check element in stack
## 6. isFull --> True or False if it has elements
## 7. delete --> delete stacks

## implementing stacks using LL is more preferrable in terms of prformance since variables are randomly assigned in memory in for LL

## stack with no size limit

class stack:

    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    ## isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    ## push method: --> using append method
    def push(self,value):
        self.list.append(value)
        return 'Element has been pushed to the stack.'
     
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

    a = stack()
    print(a.isEmpty())
    a.push(1)
    a.push(2)
    a.push(3)
    print(a.isEmpty())
    a.pop()
    a.peek()
    a.delete()
