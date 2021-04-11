import linked_list

class Stack():
    def __init__(self):
        self.stack=linked_list.LinkedList()
    def push(self, data):
        self.stack.add_node(data)
    def pop(self):
        rv=self.stack.getFirstElement()
        self.stack.remove_first_element()
        return rv
    def peek(self):
        if self.stack.head==None:
            raise ValueError("Empty stack")
        return self.stack.getFirstElement()
    def __str__(self):
        return self.stack.__str__()
    def isEmpty(self):
        return self.stack.head==None

if __name__=="__main__":
    stack=Stack()
    print(stack.isEmpty())
    # print(stack.peek())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.peek())
    print(stack)
    print(stack.pop())
    print(stack.peek())
    print(stack)
    print(stack.isEmpty())
