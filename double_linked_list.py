class DDNode():
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList():
    def __init__(self):
        self.head=None
    def add_node(self, data):
        node=DDNode(data)
        if self.head==None:
            self.head=node
        else:
            next=self.head
            next.prev=node
            node.next=next
            self.head=node
    def add_node_by_obj(self, node):
        if self.head==None:
            self.head=node
        else:
            next=self.head
            next.prev=node
            node.next=next
            self.head=node
    def __str__(self):
        head=self.head
        rv=[]
        while head!=None:
            rv.append(head.data)
            head=head.next
        return "{}".format(rv)
    def remove_first_element(self):
        if self.head:
            head=self.head
            head.next.prev=None
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
        node=DDNode(data)
        tmp=prev_node.next
        prev_node.next=node
        node.next=tmp
        node.prev=prev_node
    def delete_node(self, node):
        head=self.head
        while head!=None:
            # we've found our node to delete, set prev's next equal to head's next
            if head==node:
                next=head.next
                prev=head.prev
                if prev:
                    prev.next=next
                else:
                    self.head=self.head.next
                if next:
                    next.prev=prev
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

if __name__=="__main__":
    a=DDNode(20)
    test_DDlist=DoubleLinkedList()
    test_DDlist.add_node_by_obj(a)
    test_DDlist.add_node(5)
    test_DDlist.add_node(8)
    test_DDlist.add_node(9)
    print(test_DDlist)
    test_DDlist.delete_node(a)
    print(test_DDlist)
    test_DDlist.insert_at_pos(2, 1)
    print(test_DDlist)
    test_DDlist.updateNodeAtPos(1, 3)
    print(test_DDlist)
    test_DDlist.remove_first_element()
    print(test_DDlist)
