import heapq
from heapq import heappop, heappush

from llist import dllist, sllist

double_list=dllist([1,2,3])
print(double_list)

double_list.append(1)
print(double_list)

print(double_list.nodeat(1).value)
print(double_list.size)

node=double_list.first
print(node)
print(node.value)
print(node.prev)
print(node.next)

print("-----")

single_list=sllist([1,2,3])
print(single_list)
print(single_list.first.value)
print(single_list.first.next)

# Python Stack

stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack.pop())
print(stack)


# Python Queue

queue=[]
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print(queue.pop(0))
print(queue)

print("-------")


heap=[]
heappush(heap, 10)
heappush(heap, 4)
heappush(heap, 3)
heappush(heap, 7)
heappush(heap, 5)
heappush(heap, 9)

print(heap)
print(heappop(heap))
print(heap)
