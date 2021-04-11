# Time complexity analysis: O(N^2). why? we iterate over the input (O(N)), and for each iteration, we perform a linear number of comparisons
# Space complexity analysis: O(N). why? we are allocating no new memory, but our function must be able to store all elements of the input list. Thus, as our input list grows, the space that our algorithm uses grows proportionally.
def insertion_sort(input):
    # compare input[1] and input[0]
    # if input[1]<input[0], swap
    # go to input2, if input[2] < input[1], swap, then if input[1]<input[0], swa
    for i in range(len(input))[1:]:
        j=i
        while j>0:
            if input[j]<input[j-1]:
                swap(input, j, j-1)
            j-=1
    return input

def swap(input, i, j):
    tmp=input[i]
    input[i]=input[j]
    input[j]=tmp

    # [1, 5, 4, 3]
    # start with j=1, compare 5 and 1, don't swap, decrement j. j=0
    # go to 4. j=2, compare 4 and 5, swap and decrement j, then we have [1, 4, 5, 3], with j=1
    # then compare 4 and 1, don't swap.
    # given a value of j, we compare j and j-1 (swap if needed), decrement j. We perform this action again until we reach j=0


# Test cases
case1=[]
case2=[1,1,1,1,1]
case3=[0, 1, 2, 3]
case4=[1, 5, 2, 8, 3, 5, 10, 1]

all_cases=[case1, case2, case3, case4]
for case in all_cases:
    print("Before insertion sorting: ", case)
    insertion_sort(case)
    print("After insertion sorting:", case)
    print("---------")

print("#################################################################")

# Time complexity: O(n^2) Why? We iterate through the list O(N), and for every iterator, we perform O(N) operations (comparing with the rest of the list)
# Space complexity: O(n) Why? We need to load the full list in memory
def selection_sort(input):
    # iterate through list, find smallest element, swap with zeroth element.
    # iterate through list starting at idx=1, find smallest element, swap with idx=1 element
    for i in range(len(input)):
        j=i
        for k in range(len(input))[j+1:]:
            startElem=input[j]
            compareElem=input[k]
            if compareElem<startElem:
                swap(input, j, k)


# Test cases
case1=[]
case2=[1,1,1,1,1]
case3=[0, 1, 2, 3]
case4=[1, 5, 2, 8, 3, 5, 10, 1]

all_cases=[case1, case2, case3, case4]
for case in all_cases:
    print("Before selection sorting: ", case)
    selection_sort(case)
    print("After selection sorting:", case)
    print("---------")



# input: string, and pattern,
# output: boolean. does pattern exist in string?
# pseudo code:
# patLen=len(pattern)
# iterate from i=0 to (<) len(string)-patLen
# for each iterator i, check if string[i:patLen] equals pattern. if so, return true
def string_pattern_match(input, pattern):
    patLen=len(pattern)
    inpLen=len(input)
    for i in range(len(input)-patLen+1):
        test_pattern=input[i:i+patLen]
        if pattern==test_pattern:
            return True
    return False

print(string_pattern_match("aaaabbbb", "aaa")) # should be True
print(string_pattern_match("aaaabbbb", "aaab")) # should be True
print(string_pattern_match("aaaabbbb", "bbbb")) # should be True
print(string_pattern_match("aaaabbbb", "bbbbb")) # should be False


# Notes:
    # 1st iteration: off by 1 error (iterated over range(len(input)-patLen)) and set test_pattern to input[i:patLen] instead of input[i:i+patLen]


# input: two nested lists matrix A (dim: x*y), matrix B (y*z)
# output: nested list multiplying A and B. matrix C (x*z)
#
#
#
#
#
def matrix_multiplication(matrixA, matrixB):
    matrixC=[[0 for k in range(len(matrixB[0]))] for j in range(len(matrixA))]
    # i is iterator for rows of A (1 through x)
    for i in range(len(matrixA)):
        # k is the iterator for the columns of B (1 through z)
        for k in range(len(matrixB[0])):
            matrixC[i][k]=0
            # j is iterator for rows of A (1 through y)
            for j in range(len(matrixA[0])):
                matrixC[i][k]+=matrixA[i][j]*matrixB[j][k]
    return matrixC

print(matrix_multiplication([[1,2],[3,4],[5,6]], [[1,2,3,4],[5,6,7,8]]))
