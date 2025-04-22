a = [10,20,30,40,50,60,70,80,90]

## Approach 1:

def opertor_searh(target, myList:list):
    '''
    description: this function will use the `in` opertion to see if the target element is in the list or not.
    target: argument provided by the user
    myList: input list where we need to search the element
    reurns: boolean value

    '''

    if target in myList:
        print(f"{target} found in the input list")
        return 1
    else:
        print(f"{target} not found in he input list")
        return -1
        
print(opertor_searh(40,a))

## Approach 2:

def linear_search(target,myList1:list):
    '''
    description: we will apply enumerate function to loop through the index and the elements and then with the help of `==`, we will see if the element on the available index is\
    present or not.
    target: argument provided by the user
    myList1: input list where we need to search the element
    '''

    for idx, value in enumerate(myList1):
        if myList1[idx] == target:
            print("Input value is available in the list")
            return 1
        else:
            print("Input value is not available in the list")
            return 0
print(linear_search(30,a))