# Implement an algorithm to determine if a string has all unique chars. What if you cannot use additional data structures?
def has_unique_chars(input):
    chars={}
    for char in input:
        if char in chars:
            return False
        else:
            chars[char]=True
    return True

# Given two strings, write a method to decide if one is a permutation of the other
def is_permutation(s, t):
    # "abc", "bac"
    pass

# write a function that takes a string 'aabccccaaa' and returns 'a2b1c4a3'
def compress_string(input):
    output_str=""
    parent_idx=0
    child_idx=0
    count_equal=0
    while parent_idx<len(input):
        while(input[parent_idx]==input[child_idx]):
            count_equal+=1
            child_idx+=1
            if child_idx==len(input):
                break
        output_str+=input[parent_idx]
        output_str+=str(count_equal)
        parent_idx=child_idx
        count_equal=0
    if len(output_str)<len(input):
        return output_str
    return input



if __name__=="__main__":
    print(has_unique_chars("abcd"))
    print(has_unique_chars(""))
    print(has_unique_chars("aaaaa"))

    print("------")
    print(compress_string("aabccccaaa"))
    print(compress_string("a"))
    print(compress_string("harsha"))
    print(compress_string("hhhaaarrrssshhhhhhhhhhaaaaaahahah"))