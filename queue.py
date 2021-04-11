import linked_list

class Queue:
    def __init__(self):
        self.queue=linked_list.LinkedList()
        self.last=None
        self.first=None
    def isEmpty(self):
        return self.last==None
    def enqueue(self, data):
        node=linked_list.Node(data)
        if self.isEmpty():
            self.queue.add_node_by_obj(node)
            self.last=node
            self.first=node
            return
        self.last.next=node
        self.last=node
    def dequeue(self):
        if self.isEmpty():
            raise ValueError("queue is empty")
        rv=self.queue.getFirstElement()
        self.queue.remove_first_element()
        return rv
    def __str__(self):
        return self.queue.__str__()
    def length(self):
        return self.queue.length()

if __name__=="__main__":
    queue=Queue()
    print(queue.isEmpty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    for i in range(queue.length()):
        print(queue.dequeue())
    print(queue.isEmpty())
