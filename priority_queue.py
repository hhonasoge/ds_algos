from binary_heap import BinaryHeap

class PriorityQueue:
    def __init__(self):
        self.queue=BinaryHeap()
    # log(n) worst case (both time and space)
    def enqueue(self, elem):
        self.queue.insert_element(elem)
    # log(n) worst case (both time and space)
    def dequeue(self):
        return self.queue.extract_min()
    def peek_min(self):
        return self.queue[0]
    def isEmpty(self):
        return self.queue.isEmpty()
    def __str__(self):
        return self.queue.__str__()

if __name__=="__main__":
    pq=PriorityQueue()
    pq.enqueue(2)
    pq.enqueue(9)
    pq.enqueue(6)
    pq.enqueue(3)
    print(pq)
