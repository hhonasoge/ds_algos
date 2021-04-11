from math import floor

class BinaryHeap():
    def __init__(self):
        self.data=[]
    def get_parent_idx(self, index):
        if index==0:
            return (-1,-1)
        return (floor((index-1)/2), self.data[floor((index-1)/2)])
    def get_youngest_child(self, index):
        child_idx=index*2+1
        if child_idx>=len(self.data):
            return (-1,-1)
        return (child_idx, self.data[child_idx])
    def isEmpty(self):
        return len(self.data)==0
    def insert_element(self, elem):
        if len(self.data)==0:
            self.data.append(elem)
            return
        self.data.append(elem)
        self.bubble_up(len(self.data)-1)
    def bubble_up(self, index):
        # Time complexity: O(log(n)). why? the min heap is a COMPLETE binary tree (all levels of the tree except possibly the last are filled).
        #   This means that the height of the tree is on the order of log(n). bubble_up runs on the order of the height of the tree.
        # Space complexity: O(log(n)) why? at any point we may have up to h (where h is the height of the tree) function calls on the stack.
        parent_idx=self.get_parent_idx(index)[0]
        if parent_idx==-1:
            return
        if self.data[parent_idx]>self.data[index]:
            swap(self.data, parent_idx, index)
        self.bubble_up(parent_idx)
    def bubble_down(self, index):
        # same complexity analysis as bubble_up
        if self.isEmpty():
            return
        minIndex=index
        minElem=self.data[index]
        youngest_child_idx, youngest_child_val = self.get_youngest_child(index)
        if youngest_child_idx==-1:
            return
        if youngest_child_val<minElem:
            minIndex=youngest_child_idx
            minElem=youngest_child_val
        oldest_child_idx=youngest_child_idx+1
        if oldest_child_idx<len(self.data):
            oldest_child_val=self.data[oldest_child_idx]
            if oldest_child_val<minElem:
                minIndex=oldest_child_idx
                minElem=oldest_child_val
        if minIndex!=index:
            swap(self.data, index, minIndex)
            self.bubble_down(minIndex)
    def extract_min(self):
        if len(self.data)==0:
            raise ValueError("Heap is empty")
        min=self.data[0]
        self.data[0]=self.data[len(self.data)-1]
        self.data=self.data[0:len(self.data)-1]
        self.bubble_down(0)
        return min
    def peek_min(self):
        if len(self.data)==0:
            raise ValueError("Heap is empty")
        return self.data[0]
    def __str__(self):
        return "{}".format(self.data)
    # HEAP SORT ALGORITHM LEZZZGOOOO
    def sort(self):
        sorted_elems=[]
        while self.isEmpty() is False:
            sorted_elems.append(self.extract_min())
        return sorted_elems

# swap is a helper function that swaps two elements (specified by index) in a list
def swap(input_list, idx1, idx2):
    tmp=input_list[idx1]
    input_list[idx1]=input_list[idx2]
    input_list[idx2]=tmp



if __name__=="__main__":
    heap=BinaryHeap()
    heap.insert_element(3)
    heap.insert_element(4)
    heap.insert_element(5)
    heap.insert_element(2)
    print(heap.data)
    print("Min: ", heap.extract_min())
    print("Min: ", heap.extract_min())
    print("Min: ", heap.extract_min())
    print("Min: ", heap.extract_min())
    # print("Min: ", heap.extract_min())
    print("-------------")
    print(heap)

    # NOTE: Constructing a heap from random/unsorted data as below is O(n*log(n)) worst case where n is the length of data
    unsorted_array=[1, 10, 5, 4, 35, 82, 17, 5, 3, 3, 4]
    for i in unsorted_array:
        heap.insert_element(i)
    print(heap)

    # print("Min: ", heap.extract_min())
    # print("Min: ", heap.extract_min())
    # print("Min: ", heap.extract_min())
    # print("Min: ", heap.extract_min())
    # print("Min: ", heap.extract_min())
    # print("Min: ", heap.extract_min())
    # print("Min: ", heap.extract_min())
    # print("Min: ", heap.extract_min())
    # print("Min: ", heap.extract_min())
    # print("Min: ", heap.extract_min())
    # print("Min: ", heap.extract_min())


    rv=heap.sort()
    print(rv)


def swap(input_list, idx1, idx2):
    tmp=input_list[idx1]
    input_list[idx1]=input_list[idx2]
    input_list[idx2]=tmp
