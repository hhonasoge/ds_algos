class Node():
    def __init__(self, data):
        self.data=data
        self.next=None
    def __str__(self):
        return("Data: {}, Next: {}".format(self.data, self.next))

class LinkedList():
    def __init__(self):
        self.head=None
    def add_node(self, data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            next=self.head
            self.head=node
            node.next=next
    def add_node_by_obj(self, node):
        if self.head==None:
            self.head=node
        else:
            next=self.head
            self.head=node
            node.next=next
    def __str__(self):
        head=self.head
        rv=[]
        while head!=None:
            rv.append(head.data)
            head=head.next
        return "{}".format(rv)
    def remove_first_element(self):
        if self.head:
            self.head=self.head.next
    def length(self):
        counter=0
        head=self.head
        while head!=None:
            counter+=1
            head=head.next
        return counter
    def insert_at_pos(self, data, pos):
        if pos > self.length() or pos < 0:
            raise ValueError("position larger than length of list")
        if self.length()==0 or pos==0:
            self.add_node(data)
            return
        prev_node=self.head
        pos_counter=1
        while prev_node.next!=None:
            if pos_counter==pos:
                break
            pos_counter+=1
            prev_node=prev_node.next
        node=Node(data)
        tmp=prev_node.next
        prev_node.next=node
        node.next=tmp
    def delete_node(self, node):
        head=self.head
        prev=None
        while head!=None:
            # we've found our node to delete, set prev's next equal to head's next
            if head==node:
                if prev!=None:
                    tmp=head.next
                    prev.next=head.next
                else:
                    self.head=self.head.next
            prev=head
            head=head.next
    def getFirstElement(self):
        if self.head:
            return self.head.data
    def getPosOfNode(self, node):
        head=self.head
        pos_counter=0
        while head!=None:
            if head==node:
                return pos_counter
            pos_counter+=1
            head=head.next
        raise ValueError("node does not exist in list")
    def updateNodeAtPos(self, pos, data):
        head=self.head
        pos_counter=0
        while pos_counter!=pos:
            if head==None:
                raise ValueError("position is greater than length of list")
            if pos_counter==pos:
                break
            head=head.next
            pos_counter+=1
        head.data=data
        return




def LL_length(LList):
    if LList:
        return LList.length()
    return 0

if __name__=="__main__":
    a=Node(20)
    print(a)

    test_list=LinkedList()
    print(dir(test_list))
    test_list.add_node(5)
    test_list.add_node(8)
    test_list.add_node(9)
    test_list.insert_at_pos(2, 3)
    test_list.insert_at_pos(5, 1)
    test_list.add_node_by_obj(a)
    print(test_list.length())
    print(test_list)
    print("-------")
    print(test_list.getPosOfNode(a))
    test_list.delete_node(a)
    print(test_list)
    print(test_list.length())
    print(LL_length(test_list))
    print(test_list.updateNodeAtPos(1, 10))
    print(test_list)
    print(test_list.getFirstElement())
