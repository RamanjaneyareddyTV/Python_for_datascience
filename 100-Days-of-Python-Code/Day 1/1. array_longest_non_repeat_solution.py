# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Challenge
#
# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# ---------------------------------------------------------------

def longest_non_repeat(str):

    # init start position and max length
    i=0
    max_length = 1
    lis1 = list(str)

    for i in range(0,len(lis1)-1):
        sub_str=[]

        # continue increase sub string if did not repeat character
        while (i < len(str)) and (str[i] not in sub_str):
            sub_str.append(str[i])
            i = i + 1
        # update the max length
        if len(sub_str) > max_length:
            max_length = len(sub_str)

        print(sub_str)

    return max_length



str1 = "abcabcbb"
print(longest_non_repeat(str1))
