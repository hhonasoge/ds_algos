# Palindrome Number
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
# Example 1:

# Input: x = 121
# Output: true
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Example 4:

# Input: x = -101
# Output: false

from math import floor

def isPalindrome(x: int) -> bool:
    str_x=str(x)
    for i in range(floor(len(str_x)/2)):
        if str_x[i]!=str_x[len(str_x)-1-i]:
            return False
    return True

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))


def getLastDigit(x):
    return x%10

def removeLastDigit(x):
    return floor(x/10)

def isFuzzyEqual(x, tmp):
    if x==tmp:
        return True
    if removeLastDigit(x)==tmp:
        return True
    return False

print(getLastDigit(102))
print(removeLastDigit(102))

print("---------")

def isPalindromeNoString(x: int) -> bool:
    if x<0:
        return False
    if x<10:
        return True
    if x%10==0:
        return False
    # tmp=0. our goal is to assign temp to the last half of the chars of x, in reverse order
    # getLastDigit of x, add to tmp, removeLastDigit of x
    # then continue...
    #      multiply tmp by 10, getLastDigit, removeLastDigit, add to tmp
    # how long do we go (what's our while loop condition)? as long as tmp < x
    # how do we handle the middle character? isFuzzyEqual which checks if x,tmp are equal 
    # or if x' and tmp are equal where x' = removeLastDigit(x)
    tmp=0
    while (tmp<=x):
        if isFuzzyEqual(x, tmp):
            return True
        last_dig=getLastDigit(x)
        x=removeLastDigit(x)
        tmp*=10
        tmp+=last_dig
    return False

print(isPalindromeNoString(12))
print(isPalindromeNoString(10))
print(isPalindromeNoString(121))
print(isPalindromeNoString(1211))
print(isPalindromeNoString(-1211))
print(isPalindromeNoString(113311))

print("------")

import tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


def isSymmetric(root: tree.TreeNode) -> bool:
    if root==None:
        return True
    return isSymmetricHelper(root.left, root.right)

def isSymmetricHelper(left: tree.TreeNode, right: tree.TreeNode) -> bool:
    if left==None and right==None:
        return True
    if left==None:
        return False
    if right==None:
        return False
    if left.val!=right.val:
        return False
    return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)

root=tree.TreeNode(1)
left2=tree.TreeNode(2)
right2=tree.TreeNode(2)
root.left=left2
root.right=right2
left3=tree.TreeNode(3)
right3=tree.TreeNode(3)
left2.left=left3
right2.right=right3
left4=tree.TreeNode(4)
right4=tree.TreeNode(4)
left2.right=left4
right2.left=right4

print(isSymmetric(root))


print("-----")
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

def isIsomorphicHelper(s: str, t: str) -> bool:
    s_len=len(s)
    t_len=len(t)
    if s_len!=t_len:
        return False
    s_to_t_map={}
    for i in range(s_len):
        if s[i] not in s_to_t_map:
            s_to_t_map[s[i]]=t[i]
        else:
            if t[i]!=s_to_t_map[s[i]]:
                return False
    return True

def isIsomorphic(s: str, t: str) -> bool:
    return isIsomorphicHelper(s, t) and isIsomorphicHelper(t, s)


def isIsomorphic2(s: str, t: str) -> bool:
    s_len=len(s)
    t_len=len(t)
    if s_len!=t_len:
        return False
    s_to_t_map={}
    t_to_s_map={}
    for i in range(s_len):
        if s[i] not in s_to_t_map:
            s_to_t_map[s[i]]=t[i]
        else:
            if t[i]!=s_to_t_map[s[i]]:
                return False
        if t[i] not in t_to_s_map:
            t_to_s_map[t[i]]=s[i]
        else:
            if s[i]!=t_to_s_map[t[i]]:
                return False
    return True

print(isIsomorphic("egg", "add")) # Expected: True
print(isIsomorphic("paper", "title")) # Expected: True
print(isIsomorphic("foo", "bar")) #Expected: False
print(isIsomorphic("badc", "baba")) #Expected: False
print("*****")
print(isIsomorphic2("egg", "add")) # Expected: True
print(isIsomorphic2("paper", "title")) # Expected: True
print(isIsomorphic2("foo", "bar")) #Expected: False
print(isIsomorphic2("badc", "baba")) #Expected: False

# bbc 
# aaa



def binary_search(input, target):
    return binary_search_helper(input, 0, len(input)-1, target)

def binary_search_helper(input, left, right, target):
    if left>right:
        return -1
    mid=left+(right-left)//2
    if input[mid]==target:
        return mid
    if target<input[mid]:
        return binary_search_helper(input, left, mid-1, target)
    return binary_search_helper(input, mid+1, right, target)